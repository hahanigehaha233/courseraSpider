import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='coursera', charset='utf8')
cursor = conn.cursor()

sql1 = """create table coursera.project 
        (Id_P int NOT NULL auto_increment,
         PRIMARY KEY (Id_P),
         project_name varchar(500),
         project_key varchar(50),
         FOREIGN KEY (project_name) REFERENCES id(name),
         feedback_num varchar(10),
         t_rank integer(1))"""

sql2 = """create table coursera.id
        (id int NOT NULL auto_increment,
        PRIMARY KEY (id),
        href varchar(500),
        name varchar(500),
        UNIQUE (name))"""

cursor.execute(sql1)
cursor.execute(sql2)
conn.commit()
cursor.close()
conn.close()
