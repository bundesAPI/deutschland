# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from dwd.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from dwd.model.crowd_meldung import CROWDMeldung
from dwd.model.crowd_meldung_highest_severities import CROWDMeldungHighestSeverities
from dwd.model.crowd_meldung_meldungen import CROWDMeldungMeldungen
from dwd.model.error import Error
from dwd.model.gemeinde_warnings import GemeindeWarnings
from dwd.model.gemeinde_warnings_binnen_see import GemeindeWarningsBinnenSee
from dwd.model.gemeinde_warnings_binnen_see209901000 import GemeindeWarningsBinnenSee209901000
from dwd.model.gemeinde_warnings_warnings import GemeindeWarningsWarnings
from dwd.model.station_overview import StationOverview
from dwd.model.station_overview10865 import StationOverview10865
from dwd.model.station_overview10865_days import StationOverview10865Days
from dwd.model.station_overview10865_forecast1 import StationOverview10865Forecast1
from dwd.model.station_overview10865_forecast2 import StationOverview10865Forecast2
from dwd.model.warning_coast import WarningCoast
from dwd.model.warning_coast_warnings import WarningCoastWarnings
from dwd.model.warning_coast_warnings501000007 import WarningCoastWarnings501000007
from dwd.model.warning_nowcast import WarningNowcast
from dwd.model.warning_nowcast_regions import WarningNowcastRegions
from dwd.model.warning_nowcast_warnings import WarningNowcastWarnings
