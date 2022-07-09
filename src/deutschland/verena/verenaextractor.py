import re
from typing import Tuple

from bs4 import BeautifulSoup, element


class VerenaExtractor:
    """
    Extracts the job listings objects from the search result website of the VERENA portal.
    """

    def __init__(self, source: str):
        """
        Init with string containing the sourcecode the website (for example from request.text)
        """
        self.soup = BeautifulSoup(source, "html.parser")
        self.map_onclick_regex = re.compile(r" <b>.{0,}<\/b><br\/>")

    def extract(self):
        """
        Returns a list of all job listings contained in the sourcecode used in VerenaExtractor(source)

        Example of the json format can be found at ./example.json
        """
        ausschreibungen = self.soup.findAll("div", {"class": "ausschreibung"})
        res = []
        for aus in ausschreibungen:
            aus_parts = aus.findAll("div", {"class": "ausschreibung_teil"})
            school_id, desc = self.__extract_part1(aus_parts[0])
            (
                replacement_job_type,
                replacement_job_type_raw,
                replacement_job_title,
                subjects,
                comments,
            ) = self.__extract_part2(aus_parts[1])
            duration, hours_per_week = self.__extract_part3(aus_parts[2])
            phone, fax, homepage, email, deadline = self.__extract_part4(aus_parts[3])
            coord_system, coordinates, post_adress = self.__extract_part5(aus_parts[4])
            merged = {
                **self.__format_part1(school_id, desc),
                **self.__format_part2(
                    replacement_job_type,
                    replacement_job_type_raw,
                    replacement_job_title,
                    subjects,
                    comments,
                ),
                **self.__format_part3(duration, hours_per_week),
                **self.__format_part4(phone, fax, homepage, email, deadline),
                **self.__format_part5(coord_system, coordinates, post_adress),
            }
            res.append(merged)
        return res

    def __extract_part1(self, content) -> Tuple[str, str]:
        """Returns a tuple of (school_id : str, adress : str)

        Extracts the attributes school_id & adress from the VERENA search result.

        Should be applied to the 1. <div class="ausschreibung_teil"/> in <div class="ausschreibungen"/>
        """
        school_id = content.find("strong").text
        result_elems = []
        for desc_elems in content.contents[6:-1]:
            if type(desc_elems) == element.NavigableString:
                result_elems.append(desc_elems.strip().replace("\xa0", " "))
        desc = "\n".join(result_elems)
        return school_id, desc

    def __format_part1(self, schoold_id, desc) -> dict:
        """Returns a export-ready dict for school_id & adress"""
        return {"school_id": schoold_id, "desc": desc}

    def __extract_part2(self, content):
        # TODO add typing to return value when 3.10 is realeased
        """Returns a tuple of (replacement_job_type: str, replacement_job_type_raw: str, replacement_job_title : str, subjects : List[str], comments : str | None, )

        Should be applied to the 2. <div class="ausschreibung_teil"/> in <div class="ausschreibungen"/>
        """
        comments = None
        strong = content.findAll("strong")
        replacement_job_title = strong[0].text
        subjects = [x.text for x in strong[1:]]
        if type(content.contents[-1]) == element.NavigableString:
            comments_or_empty = content.contents[-1].strip()
            if comments_or_empty:
                comments = comments_or_empty
        replacement_job_type_raw = content.contents[0].strip()
        replacement_job_type = None
        if "AnC" in replacement_job_type_raw:
            replacement_job_type = "Aufholen nach Corona"
        elif "Vertretung" in replacement_job_type_raw:
            replacement_job_type = "Vertretung"
        return (
            replacement_job_type,
            replacement_job_type_raw,
            replacement_job_title,
            subjects,
            comments,
        )

    def __format_part2(
        self,
        replacement_job_type,
        replacement_job_type_raw,
        replacement_job_title,
        subjects,
        comments,
    ) -> dict:
        """Returns a export-ready dict for replacement_job_type, replacement_job_type_raw, replacement_job_title, subjects, comments"""
        res = {
            "replacement_job_type_raw": replacement_job_type_raw,
            "replacement_job_title": replacement_job_title,
            "subjects": subjects,
        }
        if comments:
            res["comments"] = comments
        if replacement_job_type:
            res["replacement_job_type"] = replacement_job_type
        return res

    def __extract_part3(self, content):
        """Returns a tuple of (duration : str, hours_per_week : str)

        Extracts the attributes duration & hours_per_week.

        Should be applied to the 3. <div class="ausschreibung_teil"/> in <div class="ausschreibungen"/>
        """
        content_elems = content.contents
        result_elems = []
        for elem in content_elems:
            if type(elem) == element.NavigableString:
                result_elems.append(elem.strip())
        return result_elems[1], result_elems[3]

    def __format_part3(self, duration, hours_per_week):
        return {"duration": duration, "hours_per_week": hours_per_week}

    def __extract_part4(self, content):
        # TODO add typing to return value when 3.10 is realeased
        """Returns a tuple of (phone : str | None, fax : str | None, homepage : str | None, email : str | None, deadline : str)

        Extracts the attributes phone, fax, homepage, email, deadline from the VERENA search result.
        phone, fax, homepage, email are optional and can be None.

        Should be applied to the 4. <div class="ausschreibung_teil"/> in <div class="ausschreibungen"/>
        """
        email, homepage, phone, fax = None, None, None, None
        for link in content.findAll("a"):
            if "E-Mail" in link.text:
                email = link["href"]
            elif "Homepage" in link.text:
                homepage = link["href"]
        content_arr = content.contents
        for x in content_arr:
            if type(x) == element.NavigableString:
                if "☎" in x:
                    phone = x.replace("☎", "").strip()
                elif "Fax" in x:
                    fax = x.replace("Fax", "").strip()
        deadline = content.find("strong").text
        return phone, fax, homepage, email, deadline

    def __format_part4(self, phone, fax, homepage, email, deadline) -> dict:
        """Returns a export-ready dict for phone, fax, homepage, email, deadline"""
        result = {"contact": {}, "deadline": deadline}
        if phone:
            result["contact"]["phone"] = phone
        if fax:
            result["contact"]["fax"] = fax
        if homepage:
            result["contact"]["homepage"] = homepage
        if email:
            # use urlparse, but subject is the only param anyway
            result["contact"]["mail"] = {}
            result["contact"]["mail"]["raw"] = email
            email_split = email.split("?")
            result["contact"]["mail"]["adress"] = email_split[0].replace("mailto:", "")
            result["contact"]["mail"]["subject"] = email_split[1].replace(
                "subject=", ""
            )
        return result

    def __extract_part5(self, content) -> Tuple[str, str, str]:
        """Returns a tuple of (coord_system : str, coordinates : str, post_adress : str)

        Example: ("epsg:25832", "12345, 67890", "Somestreet\n9999 SomeLocation")

        Extracts the attributes coord_system & coordinates from the VERENA search result.

        Should be applied to the 5. <div class="ausschreibung_teil"/> in <div class="ausschreibungen"/>
        """
        map_div = content.find("div", {"class": "itnrwMap"})
        data_itnrw_coords = map_div["data-itnrw-coords"]
        if not data_itnrw_coords:
            return None, None, None
        else:
            data_itnrw_coords = data_itnrw_coords[1:-1].split(";")
            coord_system = data_itnrw_coords[0]
            coords = [int(x.strip()) for x in data_itnrw_coords[1].split(",")]
            name = data_itnrw_coords[2]
            map_onclick = data_itnrw_coords[3]
            post_adress = self.map_onclick_regex.sub("", map_onclick)
            post_adress = post_adress.strip()
            post_adress = "\n".join(post_adress.split("<br/>"))
            return coord_system, coords, post_adress

    def __format_part5(self, coord_system, coordinates, post_adress) -> dict:
        """Returns a export-ready dict for coord_system, coordinates & postadress"""
        if coord_system is None and coord_system is None and post_adress is None:
            return {}
        return {
            "geolocation": {
                "coord_system": coord_system,
                "coordinates": coordinates,
                "post_adress": post_adress,
            }
        }
