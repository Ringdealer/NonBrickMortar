# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import  Field


class WebxtractionItem(scrapy.Item):
    # define the fields for your item here like:
    title = Field()
    stars = Field()
    price = Field()
    imglink = Field()
    imgname = Field()
