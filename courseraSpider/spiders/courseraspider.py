# coding=utf-8
import scrapy
import json
from courseraSpider.items import CourseraspiderItem


class courseraSpider(scrapy.Spider):
    name = "getcourseid"
    start_urls = ["https://www.coursera.org/courses?languages=en&start=20"]

    def parse(self, response):
        for (href, q) in zip(response.xpath('//*[@class="rc-OfferingCard nostyle"]'),\
                       response.xpath('//*[@class="color-primary-text headline-1-text flex-1"]/text()')):
            item = CourseraspiderItem()
            item["href"] = href.xpath('@href')
            item["name"] = q
            yield item
