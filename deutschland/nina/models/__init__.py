# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.nina.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.nina.model.ags_covid_rules import AGSCovidRules
from deutschland.nina.model.ags_covid_rules_common import AGSCovidRulesCommon
from deutschland.nina.model.ags_covid_rules_icon import AGSCovidRulesIcon
from deutschland.nina.model.ags_covid_rules_level import AGSCovidRulesLevel
from deutschland.nina.model.ags_covid_rules_regulations import AGSCovidRulesRegulations
from deutschland.nina.model.ags_covid_rules_regulations_sections import (
    AGSCovidRulesRegulationsSections,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_bund import (
    AGSCovidRulesRegulationsSectionsBUND,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_bund_icon import (
    AGSCovidRulesRegulationsSectionsBUNDIcon,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_kreis import (
    AGSCovidRulesRegulationsSectionsKREIS,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_kreis_icon import (
    AGSCovidRulesRegulationsSectionsKREISIcon,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_land import (
    AGSCovidRulesRegulationsSectionsLAND,
)
from deutschland.nina.model.ags_covid_rules_regulations_sections_land_icon import (
    AGSCovidRulesRegulationsSectionsLANDIcon,
)
from deutschland.nina.model.ags_covid_rules_rules import AGSCovidRulesRules
from deutschland.nina.model.ags_overview_result import AGSOverviewResult
from deutschland.nina.model.map_warnings import MapWarnings
