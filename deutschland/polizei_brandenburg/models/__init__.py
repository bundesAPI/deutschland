# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.polizei_brandenburg.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.polizei_brandenburg.model.news import News
from deutschland.polizei_brandenburg.model.news_data import NewsData
from deutschland.polizei_brandenburg.model.pegel import Pegel
from deutschland.polizei_brandenburg.model.pegel_data import PegelData
from deutschland.polizei_brandenburg.model.reviere import Reviere
from deutschland.polizei_brandenburg.model.reviere_data import ReviereData
from deutschland.polizei_brandenburg.model.verkehr import Verkehr
from deutschland.polizei_brandenburg.model.verkehr_data import VerkehrData
from deutschland.polizei_brandenburg.model.waldbrand import Waldbrand
from deutschland.polizei_brandenburg.model.waldbrand_data import WaldbrandData
