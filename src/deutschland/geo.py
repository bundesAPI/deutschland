import math
from typing import Dict, List

import mapbox_vector_tile
import requests

from deutschland.config import Config, module_config


class Geo:
    LEVEL = 15
    URL = "https://sgx.geodatenzentrum.de/gdz_basemapde_vektor/tiles/v1/bm_web_de_3857/"
    MVT_EXTENT = 4096

    def __init__(self, config: Config = None):
        if config is None:
            self._config = module_config
        else:
            self._config = config

    def __deg2num(self, lat_deg, lon_deg, zoom):
        lat_rad = math.radians(lat_deg)
        n = 2.0**zoom
        xtile = int((lon_deg + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
        return (xtile, ytile)

    # taken from https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Lon..2Flat._to_tile_numbers_2
    def __num2deg(self, xtile, ytile, zoom):
        n = 2.0**zoom
        lon_deg = xtile / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
        lat_deg = math.degrees(lat_rad)
        return (lat_deg, lon_deg)

    # inspired by https://github.com/mapbox/vector-tile-js/blob/master/lib/vectortilefeature.js#L129
    def __vectorToCoords(self, x, y, z, px, py):
        size = self.MVT_EXTENT * math.pow(2, z)
        x0 = self.MVT_EXTENT * x
        y0 = self.MVT_EXTENT * y

        def project(px, py):
            y2 = 180 - (y0 - py) * 360 / size
            return (
                (px + x0) * 360 / size - 180,
                360 / math.pi * math.atan(math.exp(y2 * math.pi / 180)) - 90,
            )

        return project(px, py)

    def fetch(
        self,
        top_right: List[float],
        bottom_left: List[float],
        proxies: Dict[str, str] = None,
    ):
        """
        fetch the geo data inside the area selected
        :param top_right: the top right [lat, lon] coordinates (e.g. [47.23,5.53])
        :param bottom_left: the bottom left [lat, lon] coordinates (e.g. [54.96,15.38])
        :param proxies: proxies to use for this call (e.g. {'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080'}) overwrites proxies from config
        :return:
        """

        tr = self.__deg2num(top_right[0], top_right[1], self.LEVEL)
        bl = self.__deg2num(bottom_left[0], bottom_left[1], self.LEVEL)

        # parameter has higher priority than member
        if proxies is None:
            if self._config is not None and self._config.proxy_config is not None:
                proxies = self._config.proxy_config

        data = {}

        headers = {
            "Referer": "https://adv-smart.de/map-editor/map",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        }

        parsed = {}

        for x in range(bl[0], tr[0]):
            for y in range(tr[1], bl[1]):
                url = f"{self.URL}{self.LEVEL}/{x}/{y}.pbf"
                try:
                    result = requests.get(url, headers=headers, proxies=proxies)
                    geojson = mapbox_vector_tile.decode(result.content)
                    if geojson:
                        parsed = self.__parse(geojson, x, y)
                        for k in parsed.keys():
                            if k not in data:
                                data[k] = []

                            data[k] += parsed[k]

                except Exception as e:
                    print(e)
        return parsed

    def __parse(self, data, x, y):
        bottom_left = self.__num2deg(int(x) + 1, int(y) + 1, int(self.LEVEL))
        top_right = self.__num2deg(int(x), int(y), int(self.LEVEL))

        result = {}
        for feature in data.keys():
            for i in data[feature]["features"]:
                if i["geometry"]["type"] == "Point":
                    coords = self.__vectorToCoords(
                        int(x),
                        int(y) + 1,
                        self.LEVEL,
                        i["geometry"]["coordinates"][0],
                        i["geometry"]["coordinates"][1],
                    )
                    i["geometry"]["coordinates"] = coords
                elif i["geometry"]["type"] == "Polygon":
                    for e_num, e_obj in enumerate(i["geometry"]["coordinates"]):
                        for c_num, c_obj in enumerate(e_obj):
                            coords = self.__vectorToCoords(
                                int(x), int(y) + 1, self.LEVEL, c_obj[0], c_obj[1]
                            )
                            i["geometry"]["coordinates"][e_num][c_num] = coords
                        i["geometry"]["coordinates"][e_num].append(
                            i["geometry"]["coordinates"][e_num][0]
                        )
                elif i["geometry"]["type"] == "MultiLineString":
                    for e_num, e_obj in enumerate(i["geometry"]["coordinates"]):
                        for c_num, c_obj in enumerate(e_obj):
                            coords = self.__vectorToCoords(
                                int(x), int(y) + 1, self.LEVEL, c_obj[0], c_obj[1]
                            )
                            i["geometry"]["coordinates"][e_num][c_num] = coords
                elif i["geometry"]["type"] == "MultiPolygon":
                    for e_num, e_obj in enumerate(i["geometry"]["coordinates"]):
                        for f_num, f_obj in enumerate(e_obj):
                            for c_num, c_obj in enumerate(f_obj):
                                coords = self.__vectorToCoords(
                                    int(x), int(y) + 1, self.LEVEL, c_obj[0], c_obj[1]
                                )
                                i["geometry"]["coordinates"][e_num][f_num][
                                    c_num
                                ] = coords
                            i["geometry"]["coordinates"][e_num][f_num].append(
                                i["geometry"]["coordinates"][e_num][f_num][0]
                            )

                elif i["geometry"]["type"] == "LineString":
                    for e_num, e_obj in enumerate(i["geometry"]["coordinates"]):
                        coords = self.__vectorToCoords(
                            int(x), int(y) + 1, self.LEVEL, e_obj[0], e_obj[1]
                        )
                        i["geometry"]["coordinates"][e_num] = coords
                i["type"] = "Feature"

                if feature not in result:
                    result[feature] = []
                result[feature].append(i)

        return result


if __name__ == "__main__":
    geo = Geo()
    data = geo.fetch(
        [52.530116236589244, 13.426532801586827],
        [52.50876180448243, 13.359631043007212],
    )
    print(data.keys())
    print(data["Adresse"][0])
