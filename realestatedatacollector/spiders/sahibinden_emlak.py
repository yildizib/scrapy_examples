# -*- coding: utf-8 -*-
import scrapy


class SahibindenEmlakSpider(scrapy.Spider):
    name = 'sahibinden_emlak'
    allowed_domains = ['https://sahibinden.com/satilik']

    # start_urls = [
    #    'http://sahibinden.com/satilik?pagingSize=50&pagingOffset=0&address_town=660&address_town=661&address_town=653'
    #    + '&address_town=654&address_town=655&address_town=657&address_city=48&sorting=date_desc']

    def start_requests(self):
        start = 0
        for i in range(0, 20):
            yield scrapy.Request(
                'http://sahibinden.com/satilik?pagingSize=50&pagingOffset=' + str(
                    i * 50) + '&address_town=660&address_town=661&address_town=653'
                + '&address_town=654&address_town=655&address_town=657&address_city=48&sorting=date_desc', self.parse)

    def parse(self, response):
        table = response.css('#searchResultsTable')
        tr = table.xpath('//tr[@data-id]')
        for i in tr:
            print(i)
        pass
