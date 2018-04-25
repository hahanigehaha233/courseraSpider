# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseraspiderItem(scrapy.Item):
    href = scrapy.Field()
    name = scrapy.Field()
    name_id = scrapy.Field()


class DetailSpiderItem(scrapy.Item):
    project_name = scrapy.Field()
    feedback_num = scrapy.Field()
    t_rank = scrapy.Field()


class SubMenuItem(scrapy.Item):
    parent_href = scrapy.Field()
    sub_href = scrapy.Field()