import pymysql
import courseraSpider.config
conn = pymysql.connect(host=courseraSpider.config.MYSQL_HOST, port=3306, user=courseraSpider.config.MYSQL_USER, passwd=courseraSpider.config.MYSQL_PASSWD, db=courseraSpider.config.MYSQL_DBNAME, charset='utf8')
cursor = conn.cursor()

project = """create table coursera.project 
        (Id_P int NOT NULL auto_increment,
         PRIMARY KEY (Id_P),
         project_name varchar(500),
         FOREIGN KEY (project_name) REFERENCES id(name),
         feedback_num varchar(10),
         t_rank numeric(2,1),
         href varchar(50))"""

id = """create table coursera.id
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        href varchar(500),
        name varchar(500),
        name_id varchar(50),
        UNIQUE (name))"""

sub_href = """create table coursera.sub_href
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        parent_name varchar(50),
        child_href varchar(50),
        parent_href varchar(50),
        child_name varchar(50))"""

model = """create table coursera.model
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        content varchar(1000),
        userid varchar(50),
        timestamp varchar(15),
        rating varchar(1))
"""
cursor.execute(id)
cursor.execute(project)
cursor.execute(sub_href)
cursor.execute(model)
conn.commit()
cursor.close()
conn.close()
