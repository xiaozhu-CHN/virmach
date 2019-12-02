# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import sys


class BenzhuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class VirmachItem(scrapy.Item):
    price = scrapy.Field()
    addres = scrapy.Field()
    virt = scrapy.Field()
    ram = scrapy.Field()
    cpu = scrapy.Field()
    hdd = scrapy.Field()
    bw = scrapy.Field()
    ips = scrapy.Field()
