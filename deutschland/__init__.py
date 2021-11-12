try:
        __import__('pkg_resources').declare_namespace(__name__)
except:
        from pkgutil import extend_path
        __path__ = extend_path(__path__, __name__)

from .config import Config

module_config = Config()

from .geo import Geo
from .bundesanzeiger.bundesanzeiger import Bundesanzeiger
from .handelsregister.handelsregister import Handelsregister
from .lebensmittelwarnung.lebensmittelwarnung import Lebensmittelwarnung
from .verena.verena import Verena
from .bundesnetzagentur import *
from .bundeswahlleiter.bundeswahlleiter import Bundeswahlleiter
