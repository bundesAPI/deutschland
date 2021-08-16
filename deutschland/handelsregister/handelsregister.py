from datetime import date

from deutschland import module_config, Config
from deutschland.handelsregister.registrations import Registrations
from deutschland.handelsregister.publications import Publications
from deutschland.handelsregister.publication_detail import PublicationDetail


class Handelsregister:
    def __init__(self, config: Config = None):
        if config is None:
            self._config = module_config
        else:
            self._config = config

    def search(
        self,
        keywords: str = None,
        keyword_match_option: int = 2,
        match_similar_keywords: bool = False,
        head_office_location: str = None,
        include_deleted: bool = False,
        include_new_second_branches: bool = False,
        registration_type: int = None,
        registration_number: str = None,
        court: str = None,
        legal_form: str = None,
        city: str = None,
        postal_code: str = None,
        street: str = None,
        limit: int = 100,
    ):
        """Search for companies registered with the Handelsregister.

        Parameters
        ----------
        keywords: str
          Search for space-separated keywords like company name.

        keyword_match_option: int
          Specify how an item must match the keywords.
          1 : Match must contain all keywords.
          2 : Match must contain at least one keyword.
          3 : Match's company name must equal the keyword(s).

        match_similar_keywords: bool
          Match items that include similar keywords.

        head_office_location: str
          The city where the head office of a company is located.

        include_deleted: bool
          Include deleted entries as well.

        include_new_second_branches: bool
          Include only second branches registered after the 01.01.2007.
          More info here: https://www.handelsregister.de/rp_web/help.do?Thema=zweigniederlassungen

        registration_type: int
          Type of company registration.
          Possible values: HRA, HRB, GnR, PR, VR

        registration_number: str
          The number of the registration.

        court: str
          The court where the company is registered.

        legal_form: str
          The legal form of the company.
          All possible values can be found in the 'params.md' file.

        city: str
          The city of the head office or branch.
          This can be combined with 'head_office_location' like:
          "match branches which are located in 'city' whose head office
          is located in 'head_office_location'"

        postal_code: str
          The postal code of the head office or branch.

        street: str
          The street of the head office or branch.

        limit: int
          The amount of results to return.
          Defaults to 100.
        """
        params = {
            "schlagwoerter": keywords,
            "schlagwortOptionen": keyword_match_option,
            "suchOptionenAehnlich": match_similar_keywords,
            "niederlassung": head_office_location,
            "suchOptionenGeloescht": include_deleted,
            "suchOptionenNurZNneuenRechts": include_new_second_branches,
            "registerArt": registration_type,
            "registerNummer": registration_number,
            "registergericht": court,
            "rechtsform": legal_form,
            "postleitzahl": postal_code,
            "ort": city,
            "strasse": street,
            "ergebnisseProSeite": limit,
        }
        r = Registrations(self._config)
        return r.search_with_raw_params(params)

    def search_publications(
        self,
        county_code: str = None,
        court_code: str = None,
        court_name: str = None,
        from_date: date = None,
        until_date: date = None,
        company_name: str = None,
        head_office_location: str = None,
        registration_type: str = None,
        registration_number: str = None,
        publication_type: int = 0,
        order_by: int = 4,
        detailed_search: bool = False,
    ):
        """
        Search all publications by the Handelsregister.

        Broad searches (e.g. find publications for all counties and all courts)
        are only available for the past 4 weeks. If you want to search for older
        publications, you must set 'detailed_search' to 'True' and provide the
        'county_code', 'court_code', 'court_name' parameters, and at least one
        of the following: 'company_name', 'head_office_location',
        or 'registration_type' and 'registration_number'.

        Parameters
        ----------
        county_code: str
          The county code in which to search.

          Valid options are:
          by: Bayern
          be: Berlin
          br: Brandenburg
          hb: Bremen
          hh: Hamburg
          he: Hessen
          mv: Mecklenburg-Vorpommern
          ni: Niedersachsen
          nw: Nordrhein-Westfalen
          rp: Rheinland-Pfalz
          sl: Saarland
          sn: Sachsen
          st: Sachsen-Anhalt
          sh: Schleswig-Holstein
          th: Thüringen

        court_code: str
          The code for the court as specified in 'params.md'.
          Both, the court code and the court name must be provided.

        court_name: str
          The name of the court as specified in 'params.md'.
          Both, the court code and the court name must be provided.

        from_date: date
          Search for entries published after this date.
          Publications older than 4 weeks can only be searched as
          a 'detailed_search' as described above.

        until_date: date
          Search for entries published before this date.

        company_name: str
          The name of the company. Must be an exact match.

        head_office_location: str
          The city where the head office of the company is located.

        registration_type: str
          The type of the company registration.
          Valid types are:
          "HRA", "HRB", "GnR", "VR", "PR", "AR"

        registration_number: str
          The number of the company registration.

        publication_type: int
          The type of publication to search for.
          Valid options are:
          0 : All types of publications
          1 : New registrations
          2 : Registration changes
          3 : Registrations deleted by the court
          4 : Deletion announcements
          5 : Deletions
          6 : Granted Permissions
          7 : Other procedures

        order_by: int
          How to order the publication results.
          Valid options are:
          1 : Registration Number
          2 : Company name
          3 : Order by creation date of publication
          4 : Order by publication date
        """
        if (
            detailed_search
            and not (county_code and court_code and court_name)
            and not (
                company_name
                or head_office_location
                or (registration_type and registration_number)
            )
        ):
            raise Exception(
                """
                In the detailed search, you must provide 'county_code', 
                'court_code', and 'court_name' as well
                as either 'company_name', 'head_office_location' or
                'registration_type' and 'registration_number'.
                """
            )

        reg_code = (
            {
                "HRA": "A",
                "HRB": "B",
                "GnR": "G",
                "VR": "V",
                "PR": "P",
                "AR": "AR",
            }[registration_type]
            if registration_type
            else None
        )

        params = {
            "suchart": "detail" if detailed_search else "uneingeschr",
            "land": county_code,
            "gericht": court_code,
            "gericht_name": court_name,
            "vt": from_date.day if from_date else None,
            "vm": from_date.month if from_date else None,
            "vj": from_date.year if from_date else None,
            "bt": until_date.day if until_date else None,
            "bm": until_date.day if until_date else None,
            "bj": until_date.day if until_date else None,
            "fname": company_name,
            "fsitz": head_office_location,
            "rubrik": reg_code,
            "az": registration_number,
            "gegenstand": publication_type,
            "order": order_by,
        }

        p = Publications(self._config)
        return p.search_with_raw_params(params)

    def get_publication_detail(self, publication_id: str, county_code: str):
        """
        Get the details of a publication with its identifier and county code.

        Parameters
        ----------
        publication_id : str
          The identifier of the publication.
          It is usually a 6 to 7 digit number.

        county_code : str
          The code of the county in which to search for publications.

          Valid options are:
          by: Bayern
          be: Berlin
          br: Brandenburg
          hb: Bremen
          hh: Hamburg
          he: Hessen
          mv: Mecklenburg-Vorpommern
          ni: Niedersachsen
          nw: Nordrhein-Westfalen
          rp: Rheinland-Pfalz
          sl: Saarland
          sn: Sachsen
          st: Sachsen-Anhalt
          sh: Schleswig-Holstein
          th: Thüringen
        """
        pd = PublicationDetail(self._config)
        return pd.get_detail(publication_id=publication_id, county_code=county_code)


if __name__ == "__main__":
    hr = Handelsregister()
    # res = hr.search(keywords="Deutsche Bahn Aktiengesellschaft", keyword_match_option=3)
    res = hr.search_publications()
    print(res)
