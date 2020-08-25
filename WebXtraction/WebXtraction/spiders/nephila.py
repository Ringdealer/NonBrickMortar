import scrapy
from scrapy.loader import ItemLoader
from ..items import WebxtractionItem
from urllib.error import HTTPError


class NephilaSpider(scrapy.Spider):
    name = 'nephila'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def start_requests(self):
        """This method follows the page returned by the site search function"""
        search_text = 'earphones'  # This variable contains the searched item

        try:
            url = "https://www.amazon.com/s?k={0}&ref=nb_sb_noss_2".format(search_text)
        except HTTPError as e:
            print(e)
        else:
            yield scrapy.Request(url, callback=self.parse_item, meta={"search_text": search_text})

    def parse_item(self, response):
        ''' This method parses a product page
        @url https://www.amazon.com/s?k=earphones&ref=nb_sb_noss_2.html
        @returns items 1
        @scrapes title stars price imglink imgname
        '''
        l = ItemLoader(item=WebxtractionItem(), response=response)
        l.add_css('title', '.a-size-medium.a-text-normal ::text')
        l.add_css('stars', '.aok-align-bottom ::text')
        l.add_css('price', '.a-price-whole::text')
        l.add_css('imglink', '.s-image::attr(src)')
        l.add_css('imgname', '.s-image::attr(src)', re=r'\b\d[0-9]([^\.]*)')

        yield l.load_item()
