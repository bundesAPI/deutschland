import csv
import io
import zipfile
from itertools import repeat, zip_longest

import numpy as np
import pandas
import requests
from more_itertools import consume, take


class Bundeswahlleiter:
    HISTORICAL_RESULTS_URL = "https://www.bundeswahlleiterin.de/en/dam/jcr/ce2d2b6a-f211-4355-8eea-355c98cd4e47/btw_kerg.zip"
    OPEN_DATA_URL = "https://www.bundeswahlleiterin.de/bundestagswahlen/2021/ergebnisse/opendata/btw21/20240211_wdhwahl-vgl2021/csv/kerg.csv"

    def load_results(self, year):
        if year < 2021:
            buffer = self._load_historical_year(year)
        else:
            buffer = self._load_open_data()
        return self._parse_btw_results(buffer, year)

    def _parse_btw_results(self, f, year):
        encoding = "windows-1252" if year <= 2013 else "utf8"
        reader = csv.reader(
            io.TextIOWrapper(io.BytesIO(f), encoding=encoding), delimiter=";"
        )
        line_skip = 5 if year <= 2017 else 2
        consume(reader, line_skip)
        header_lines = take(3, reader)
        headers = list(zip_longest(*header_lines, fillvalue=""))
        for i in range(1, len(headers)):
            # extend implicit headers
            if not headers[i][0] and headers[i] != ("", "", ""):
                headers[i] = (
                    headers[i - 1][0],
                    headers[i][1] or headers[i - 1][1],
                    headers[i][2],
                )
        # first three columns are not named consistently
        headers[0] = ("id", "", "")
        headers[1] = ("name", "", "")
        headers[2] = ("parent", "", "")
        index = pandas.MultiIndex.from_tuples(headers)
        districts = pandas.DataFrame.from_records(list(reader), columns=index)
        contains_last_results = any(map(lambda x: "Vorperiode" in x, headers))
        if contains_last_results:
            districts.drop("Vorperiode", level=2, inplace=True, axis=1)
        if ("", "", "") in headers:
            districts.drop(("", "", ""), inplace=True, axis=1)
        districts = districts[~districts["id"].isin(["", None])]
        districts[districts == ""] = "0"
        # columns from index 3 on contain vote counts
        districts = districts.astype(
            dict(zip(districts.columns[3:], repeat(np.uint64)))
        )
        districts = districts.droplevel(2, axis=1)
        return districts

    def _load_historical_year(self, year):
        with zipfile.ZipFile(io.BytesIO(self._load_historical())) as zfile:
            filename = f"btw{year}_kerg.csv"
            if filename not in map(lambda f: f.filename, zfile.infolist()):
                raise RuntimeError(f"year {year} not available")
            with zfile.open(filename, "r") as f:
                return f.read()

    def _load_historical(self):
        resp = requests.get(self.HISTORICAL_RESULTS_URL)
        resp.raise_for_status()
        return resp.content

    def _load_open_data(self):
        resp = requests.get(self.OPEN_DATA_URL)
        resp.raise_for_status()
        return resp.content
