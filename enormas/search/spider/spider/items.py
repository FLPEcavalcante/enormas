import scrapy

from enormas.search.users.models import DataModel
from scrapy_djangoitem import DjangoItem



class DataItem(DjangoItem):

    django_model = DataModel
    
    url = scrapy.Field()
    contente = scrapy.Field()
    created_at = scrapy.Field()
