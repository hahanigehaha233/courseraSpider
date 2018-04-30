#!/usr/bin/python
#coding:utf-8
import urlparse
import urllib
import scrapy
import json
import re
from courseraSpider.pipelines import FeedbackSpiderPipeline
from courseraSpider.items import FeedbackSpiderItem
class feedbackSpider(scrapy.Spider):
    name = "getcoursefeedback"
    start_urls = []
    url = "https://www.coursera.org/api/feedback.v1/?q=course&courseId="
    para = "&feedbackSystem=STAR&ratingValues=1%2C2%2C3%2C4%2C5&categories=generic&start=0&limit=20"
    dict = FeedbackSpiderPipeline.get_project_url()
    for i in dict:
        start_urls.append(str(url+FeedbackSpiderPipeline.init_start_urls(i[0])[0][0]+para))

    def process_content(self, tmp):
        tmp = tmp.replace('<text>', '')
        tmp = tmp.replace('<text/>', '')
        tmp = tmp.replace('</text>', '')
        tmp = tmp.replace('<co-content>', '')
        tmp = tmp.replace('</co-content>', '')
        return tmp

    def parse(self, response):
            json_data = json.loads(response._body)
            for data in json_data['elements']:
                item = FeedbackSpiderItem()
                item['content'] = self.process_content(data['comments']['generic']['definition']['value'])
                item['userid'] = re.search('^\d+', data['id']).group()
                item['timestamp'] = data['timestamp']
                item['rating'] = data['rating']['value']
                item['table_name'] = re.search('/\w*$', FeedbackSpiderPipeline.find_name_from_id(str(data['context']['definition']['courseId']))[0][0].replace('-', '_')).group()[1::]
                yield item
            if(json_data['paging']['next']):
                bits = list(urlparse.urlparse(response.url))
                qs = urlparse.parse_qs(bits[4])
                qs['start'][0] = str(int(qs['limit'][0]) + int(qs['start'][0]))
                bits[4] = urllib.urlencode(qs, True)
                r_url = urlparse.urlunparse(bits)
                yield scrapy.Request(r_url)


