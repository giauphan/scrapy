# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    source = scrapy.Field()

    pass
