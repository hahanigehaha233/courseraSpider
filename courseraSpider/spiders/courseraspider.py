# coding=utf-8
import scrapy
import json
from courseraSpider.items import CourseraspiderItem
from courseraSpider.config import MAX_COURSE_PAGE


class courseraSpider(scrapy.Spider):
    name = "getcourseid"

    def start_requests(self):
        url = "https://www.coursera.org/courses?_facet_changed_=true&start="
        yield scrapy.Request(url+str(0))

    def parse(self, response):
        ''' loop in course list'''
        for (href, q) in zip(response.xpath('//*[@class="rc-OfferingCard nostyle"]'), \
                             response.xpath('//*[@class="color-primary-text headline-1-text flex-1"]/text()')):
            item = CourseraspiderItem()
            '''select column in div'''
            item["href"] = href.xpath('@href').extract()
            item["name"] = q.extract()
            js = json.loads(href.xpath('@data-click-value').extract()[0])
            item["name_id"] = js['id']
            yield item
        self.count = self.count + 1
        if (self.count <= MAX_COURSE_PAGE):
            yield scrapy.Request(self.url + str(20 * self.count))
