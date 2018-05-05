import scrapy
from courseraSpider.items import DetailSpiderItem, SubMenuItem
from courseraSpider.pipelines import DetailSpiderPipeline
import json
import re


class detailSpider(scrapy.Spider):
    name = "getcoursedetail"
    url = "https://www.coursera.org"
    start_urls = []
    dict = DetailSpiderPipeline.init_project_url()
    for i in dict:
        start_urls.append(url + i[0])

    def parse(self, response):
        if (re.search('/learn/', str(response))):
            item = DetailSpiderItem()
            item['project_name'] = response.xpath('//*[@id="rendered-content"]/div/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/h1/text()').extract()[
                0]
            num = response.xpath('//*[@id="ratings"]/div[2]/button/span/span/text()').extract()[0]
            if(num):
                item['feedback_num'] = num
            else:
                item['feedback_num'] = '2'
            item['t_rank'] = re.search('[0-5][.][0-9]', response.xpath('//*[@id="ratings"]/div[2]/div[1]/div[2]/span/text()').extract()[0]).group()
            item['href'] = str(response)[29:-1]
            yield item
        else:
            parent_href = json.loads(response.xpath('//*[@id="c-ph-right-nav"]/ul/li[4]/a/@data-click-value').extract()[0])['href']['pathname']
            parent_name_temp =response.xpath('//*[@id="rendered-content"]/div/div/div[1]/div[2]/div/main/div/h1/span/text()')
            if(parent_name_temp):
                parent_name = parent_name_temp
            else:
                parent_name = response.xpath('//*[@id="rendered-content"]/div/div/div[1]/div[2]/div/main/div/h1/text()').extract()[0]
            for (sel, name) in zip(response.xpath('//*[@class="link-to-cdp"]/span/a'), response.xpath('//*[@class="course-name headline-5-text"]/text()')):
                item = SubMenuItem()
                item['sub_href'] = sel.xpath('@href').extract()[0]
                item['sub_name'] = name.extract()
                item['parent_href'] = parent_href
                item['parent_name'] = parent_name
                yield item

