import scrapy
import json

from enormas.search.users.models import DataModel

from . import settings
from .utils import TagParser


class ScriptSpider(scrapy.Spider):
    """Link data extraction class.

    Args:
        scrapy (Spider): Spider extract the data.

    Returns:
        JSON: Return a Json file with data.

    Yields:
        dict: Extracts yield data in Json list format.
    """
    name = 'sinj'
    allowed_domains = ['www.sinj.df.gov.br']

    def start_requests(self):
        """Method to extract data from many urls.

        Yields:
            urls: Fetch data from selected urls. 
        """
        urls = [settings.URL_LUOS, 
                settings.URL_PDOT, 
                settings.URL_ZEE]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Method the extraction scrapy of url.

        Args:
            Response (dict): return response dict in Json.

        Yields:
            dict: Extracts yield data in Json list format.
        """

        data = {}
        for i in response.css('.linkname').xpath("@id").extract():
            data[i] = response.css(f'p[linkname="{i}"]::text').extract()

        for key in data.keys():
            if len(data[key]):
                data[key] = data[key][0]
        list_links = response.css('p,linkname').extract()

        for link in list_links:
            TagParser().feed(link)
            link_value = TagParser.get()
            if link_value:
                data[f'{link_value["linkname"]}_link'] = link_value["link"]

        url = response.url

        file_name = settings.os.path.basename(url).split('.')[0] + '.json'

        data_model = DataModel(url=response.url, content=data)
        data_model.save()

        with open(file_name, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)

        return data
