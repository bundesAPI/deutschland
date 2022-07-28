def test_all_imports():
    from deutschland.autobahn.apis import DefaultApi
    from deutschland.bundesanzeiger import Bundesanzeiger
    from deutschland.bundesnetzagentur import Rufzeichen
    from deutschland.bundesrat.apis import DefaultApi
    from deutschland.bundestag.apis import DefaultApi
    from deutschland.bundestag_lobbyregister.apis import DefaultApi
    from deutschland.destatis.apis import DefaultApi
    from deutschland.dip_bundestag.apis import DefaultApi
    from deutschland.dwd.apis import DefaultApi
    from deutschland.interpol.apis import DefaultApi
    from deutschland.jobsuche.apis import DefaultApi
    from deutschland.ladestationen.apis import DefaultApi
    from deutschland.mudab.apis import DefaultApi
    from deutschland.nina.apis import DefaultApi
    from deutschland.pegel_online.apis import WaterApi
    from deutschland.polizei_brandenburg.apis import DefaultApi
    from deutschland.presseportal import PresseportalApi
    from deutschland.risikogebiete.apis import DefaultApi
    from deutschland.smard.apis import DefaultApi
    from deutschland.strahlenschutz.apis import DefaultApi
    from deutschland.travelwarning.apis import DefaultApi
    from deutschland.zoll.apis import DefaultApi
    from deutschland.feiertage.apis import DefaultApi
    from deutschland.marktstammdaten.apis import DatenApi
    from deutschland.marktstammdaten.apis import FilterApi
    from deutschland.vag.api.abfahrten_api import AbfahrtenApi
    from deutschland.vag.api.fahrten_api import FahrtenApi
    from deutschland.vag.api.haltestellen_api import HaltestellenApi
    from deutschland.bundeshaushalt.api.budget_data_api import BudgetDataApi
    from deutschland.abfallnavi.api.abholpunkte_api import AbholpunkteApi
    from deutschland.abfallnavi.api.fraktionen_api import FraktionenApi
    from deutschland.abfallnavi.api.termine_api import TermineApi
    from deutschland.EcoVisio.api.default_api import DefaultApi

def test_package_imports():
    from deutschland.bundesanzeiger import Bundesanzeiger
    from deutschland.bundesnetzagentur.rufzeichen import Rufzeichen
    from deutschland.bundeswahlleiter import Bundeswahlleiter
    from deutschland.handelsregister import Handelsregister
    from deutschland.handelsregister.registrations import Registrations
    from deutschland.lebensmittelwarnung import Lebensmittelwarnung
    from deutschland.verena import Verena


def test_failing_imports():
    with pytest.raises(ImportError, match="cannot import name 'GibtsJaGarNicht'"):
        from deutschland.bundesanzeiger import GibtsJaGarNicht
