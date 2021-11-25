# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.mudab.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.mudab.model.compartment import Compartment
from deutschland.mudab.model.filter import Filter
from deutschland.mudab.model.filter_action import FilterAction
from deutschland.mudab.model.filter_request import FilterRequest
from deutschland.mudab.model.helcom_plc_station import HelcomPLCStation
from deutschland.mudab.model.inline_response200 import InlineResponse200
from deutschland.mudab.model.inline_response2001 import InlineResponse2001
from deutschland.mudab.model.inline_response2002 import InlineResponse2002
from deutschland.mudab.model.inline_response2003 import InlineResponse2003
from deutschland.mudab.model.inline_response2004 import InlineResponse2004
from deutschland.mudab.model.inline_response2005 import InlineResponse2005
from deutschland.mudab.model.inline_response2006 import InlineResponse2006
from deutschland.mudab.model.inline_response2007 import InlineResponse2007
from deutschland.mudab.model.inline_response2008 import InlineResponse2008
from deutschland.mudab.model.messstation import Messstation
from deutschland.mudab.model.orderby import Orderby
from deutschland.mudab.model.parameter import Parameter
from deutschland.mudab.model.parameter_value import ParameterValue
from deutschland.mudab.model.project_station import ProjectStation
from deutschland.mudab.model.range import Range
