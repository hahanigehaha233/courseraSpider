# coding=utf-8
import scrapy
import json
from courseraSpider.items import CourseraspiderItem
from courseraSpider.config import MAX_COURSE_PAGE

class courseraSpider(scrapy.Spider):
    name = "getcourseid"
    url = "https://www.coursera.org/courses?languages=en&start="
    count = 1
    start_urls = [url+str(0)]
    def parse(self, response):
        for (href, q) in zip(response.xpath('//*[@class="rc-OfferingCard nostyle"]'),\
                       response.xpath('//*[@class="color-primary-text headline-1-text flex-1"]/text()')):
            item = CourseraspiderItem()
            item["href"] = href.xpath('@href').extract()
            item["name"] = q.extract()
            yield item
        self.count = self.count+1
        if (self.count <= MAX_COURSE_PAGE):
            yield scrapy.Request(self.url+str(20*self.count))
