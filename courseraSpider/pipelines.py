#!/usr/bin/python
#coding:utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import config
import pymysql


class FeedbackSpiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host=config.MYSQL_HOST, port=3306, db=config.MYSQL_DBNAME,
                                       user=config.MYSQL_USER, passwd=config.MYSQL_PASSWD, charset='utf8',
                                       use_unicode=True)
        self.cursor = self.connect.cursor()

    @classmethod
    def get_project_url(cls):
        project_href = CourseraspiderPipeline()
        project_href.cursor.execute("""select href from project""")
        result = project_href.cursor.fetchall()
        project_href.connect.commit()
        project_href.connect.close()
        return result

    @classmethod
    def find_name_from_id(cls,name_id):
        name = CourseraspiderPipeline()
        name.cursor.execute("""select href from id where name_id = %s""", name_id)
        result = name.cursor.fetchall()
        name.connect.commit()
        name.connect.close()
        return result

    @classmethod
    def init_start_urls(cls, dict):
        project_key = CourseraspiderPipeline()
        project_key.cursor.execute("""select name_id from id where href = (%s)""", dict)
        result = project_key.cursor.fetchall()
        project_key.connect.commit()
        project_key.connect.close()
        return result

    def get_time_from_increment(self, table_name):
        getTimeSql = """select timestamp from increment_field where name = '{0}'""".format(table_name)
        self.cursor.execute(getTimeSql)
        data = self.cursor.fetchall()
        return data


    def process_item(self, item, spider):
        try:
            old_time = self.get_time_from_increment(item['table_name'])
            if old_time:
                if old_time[0][0] > str(item['timestamp'])[:10]:
                    return item
            findsql = "create table if not exists {0} like model".format(item['table_name'])
            self.cursor.execute(findsql)
            sql = """insert into {0}(content, userid, timestamp, rating) value('{1}',{2},{3},{4})""".format(item['table_name'], item['content'].encode("utf8"), item['userid'], str(item['timestamp'])[:10], item['rating'])
            print sql
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as error:
            spider.log(error)
        return item

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
                """insert into id(name, href, name_id)
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
                """insert into project(project_name,feedback_num,t_rank, href)
                value(%s, %s, %s, %s)""",
                (item['project_name'],
                 item['feedback_num'],
                 item['t_rank'],
                 item['href']))
            self.connect.commit()
        except Exception as error:
            spider.log(error)
        return item
