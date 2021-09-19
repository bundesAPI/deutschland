# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from polizei-brandenburg.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from polizei-brandenburg.model.news import News
from polizei-brandenburg.model.news_data import NewsData
from polizei-brandenburg.model.pegel import Pegel
from polizei-brandenburg.model.pegel_data import PegelData
from polizei-brandenburg.model.reviere import Reviere
from polizei-brandenburg.model.reviere_data import ReviereData
from polizei-brandenburg.model.verkehr import Verkehr
from polizei-brandenburg.model.verkehr_data import VerkehrData
from polizei-brandenburg.model.waldbrand import Waldbrand
from polizei-brandenburg.model.waldbrand_data import WaldbrandData
