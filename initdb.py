import pymysql
import courseraSpider.config
conn = pymysql.connect(host=courseraSpider.config.MYSQL_HOST, port=3306, user=courseraSpider.config.MYSQL_USER, passwd=courseraSpider.config.MYSQL_PASSWD, db=courseraSpider.config.MYSQL_DBNAME, charset='utf8')
cursor = conn.cursor()

sql1 = """create table coursera.project 
        (Id_P int NOT NULL auto_increment,
         PRIMARY KEY (Id_P),
         project_name varchar(500),
         FOREIGN KEY (project_name) REFERENCES id(name),
         feedback_num varchar(10),
         t_rank numeric(2,1),
         href varchar(50),
         table_name varchar(50))"""

sql2 = """create table coursera.id
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        href varchar(500),
        name varchar(500),
        name_id varchar(50),
        UNIQUE (name))"""

sql3 = """create table coursera.sub_href
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        parent_name varchar(50),
        child_href varchar(50),
        parent_href varchar(50),
        child_name varchar(50))"""

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
conn.commit()
cursor.close()
conn.close()
