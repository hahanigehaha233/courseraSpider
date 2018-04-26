# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import config
import pymysql


class SubMenuspiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host=config.MYSQL_HOST, port=3306, db=config.MYSQL_DBNAME,
                                       user=config.MYSQL_USER, passwd=config.MYSQL_PASSWD, charset='utf8',
                                       use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into sub_href(parent_href, child_href, parent_name, child_name)
                value (%s, %s, %s, %s)""",
                (item['parent_href'],
                 item['sub_href'],
                 item['parent_name'],
                 item['sub_name']))
            self.connect.commit()
        except Exception as error:
            spider.log(error)
        return item


class CourseraspiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host=config.MYSQL_HOST, port=3306, db=config.MYSQL_DBNAME,
                                       user=config.MYSQL_USER, passwd=config.MYSQL_PASSWD, charset='utf8',
                                       use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into id(name, href)
                value (%s, %s, %s)""",
                (item['name'],
                 item['href'],
                 item['name_id']))
            self.connect.commit()
        except Exception as error:
            spider.log(error)
        return item


class DetailSpiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host=config.MYSQL_HOST, port=3306, db=config.MYSQL_DBNAME,
                                       user=config.MYSQL_USER, passwd=config.MYSQL_PASSWD, charset='utf8',
                                       use_unicode=True)
        self.cursor = self.connect.cursor()

    @classmethod
    def init_project_url(cls):
        table_id = CourseraspiderPipeline()
        table_id.cursor.execute("""select href from id""")
        result = table_id.cursor.fetchall()
        table_id.connect.commit()
        table_id.connect.close()
        return result

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into project(project_name,feedback_num,t_rank,has_table, href)
                value(%s, %s, %s, 0, %s)""",
                (item['project_name'],
                 item['feedback_num'],
                 item['t_rank'],
                 item['href']))
            self.connect.commit()
        except Exception as error:
            spider.log(error)
        return item
