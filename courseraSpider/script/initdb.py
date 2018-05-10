import pymysql
import courseraSpider.config

conn = pymysql.connect(host=courseraSpider.config.MYSQL_HOST, port=3306, user=courseraSpider.config.MYSQL_USER,
                       passwd=courseraSpider.config.MYSQL_PASSWD, db=courseraSpider.config.MYSQL_DBNAME, charset='utf8')
cursor = conn.cursor()

project = """create table {0}.project 
        (Id_P int NOT NULL auto_increment,
         PRIMARY KEY (Id_P),
         project_name varchar(500),
         feedback_num varchar(10),
         t_rank numeric(2,1),
         href varchar(50))""".format(courseraSpider.config.MYSQL_DBNAME)

id = """create table {0}.id
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        href varchar(500),
        name varchar(500),
        name_id varchar(50))""".format(courseraSpider.config.MYSQL_DBNAME)

sub_href = """create table {0}.sub_href
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        parent_name varchar(50),
        child_href varchar(50),
        parent_href varchar(50),
        child_name varchar(50))""".format(courseraSpider.config.MYSQL_DBNAME)

model = """create table {0}.model
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        content varchar(1000),
        userid varchar(50),
        UNIQUE (userid),
        timestamp varchar(15),
        rating varchar(1))""".format(courseraSpider.config.MYSQL_DBNAME)

increment_field = """create table {0}.increment_field
        (id int not null auto_increment,
        PRIMARY KEY (id),
        timestamp varchar(15),
        name varchar(50))""".format(courseraSpider.config.MYSQL_DBNAME)

cursor.execute(id)
cursor.execute(project)
cursor.execute(sub_href)
cursor.execute(model)
cursor.execute(increment_field)
conn.commit()
cursor.close()
conn.close()
