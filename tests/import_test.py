import pytest


def test_all_imports():
    from deutschland.abfallnavi.api.abholpunkte_api import AbholpunkteApi  # noqa: F401
    from deutschland.abfallnavi.api.fraktionen_api import FraktionenApi  # noqa: F401
    from deutschland.abfallnavi.api.termine_api import TermineApi  # noqa: F401
    from deutschland.autobahn.apis import DefaultApi  # noqa: F401
    from deutschland.bundesanzeiger import Bundesanzeiger  # noqa: F401
    from deutschland.bundeshaushalt.api.budget_data_api import BudgetDataApi  # noqa: F401
    from deutschland.bundesnetzagentur import Rufzeichen  # noqa: F401
    from deutschland.bundesrat.apis import DefaultApi  # noqa: F401
    from deutschland.bundestag.apis import DefaultApi  # noqa: F401
    from deutschland.bundestag_lobbyregister.apis import DefaultApi  # noqa: F401
    from deutschland.destatis.apis import DefaultApi  # noqa: F401
    from deutschland.dip_bundestag.apis import PlenarprotokolleApi  # noqa: F401
    from deutschland.dwd.apis import DefaultApi  # noqa: F401
    from deutschland.EcoVisio.api.default_api import DefaultApi  # noqa: F401
    from deutschland.feiertage.apis import DefaultApi  # noqa: F401
    from deutschland.interpol.apis import DefaultApi  # noqa: F401
    from deutschland.jobsuche.apis import DefaultApi  # noqa: F401
    from deutschland.ladestationen.apis import DefaultApi  # noqa: F401
    from deutschland.marktstammdaten.apis import DatenApi, FilterApi  # noqa: F401
    from deutschland.mudab.apis import DefaultApi  # noqa: F401
    from deutschland.nina.apis import DefaultApi  # noqa: F401
    from deutschland.pegel_online.apis import WaterApi  # noqa: F401
    from deutschland.polizei_brandenburg.apis import DefaultApi  # noqa: F401
    from deutschland.risikogebiete.apis import DefaultApi  # noqa: F401
    from deutschland.smard.apis import DefaultApi  # noqa: F401
    from deutschland.strahlenschutz.apis import DefaultApi  # noqa: F401
    from deutschland.travelwarning.apis import DefaultApi  # noqa: F401
    from deutschland.vag.api.abfahrten_api import AbfahrtenApi  # noqa: F401
    from deutschland.vag.api.fahrten_api import FahrtenApi  # noqa: F401
    from deutschland.vag.api.haltestellen_api import HaltestellenApi  # noqa: F401
    from deutschland.zoll.apis import DefaultApi  # noqa: F401


def test_package_imports():
    from deutschland.bundesanzeiger import Bundesanzeiger  # noqa: F401
    from deutschland.bundesnetzagentur.rufzeichen import Rufzeichen  # noqa: F401
    from deutschland.bundeswahlleiter import Bundeswahlleiter  # noqa: F401
    from deutschland.lebensmittelwarnung import Lebensmittelwarnung  # noqa: F401
    from deutschland.verena import Verena  # noqa: F401


def test_failing_imports():
    with pytest.raises(ImportError, match="cannot import name 'GibtsJaGarNicht'"):
        from deutschland.bundesanzeiger import GibtsJaGarNicht  # noqa: F401
