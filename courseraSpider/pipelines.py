# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import config
import pymysql


class CourseraspiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host=config.MYSQL_HOST, port=3306, db=config.MYSQL_DBNAME, user=config.MYSQL_USER, passwd=config.MYSQL_PASSWD, charset='utf8', use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into id(name, href)
                value (%s, %s)""",
                (item['name'],
                 item['href']))
            self.connect.commit()
        except Exception as error:
            spider.log(error)
            pass
        return item
