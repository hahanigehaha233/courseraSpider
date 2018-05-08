import pymysql
import config
conn = pymysql.connect(host=config.MYSQL_HOST, port=3306, user=config.MYSQL_USER, passwd=config.MYSQL_PASSWD, db=config.MYSQL_DBNAME, charset='utf8')
cursor = conn.cursor()

sql = """show tables;"""
cursor.execute(sql)
result = cursor.fetchall()
for i in result:
    print i[0]
    if i[0] in ('project', 'id', 'sub_href', 'increment'):
        continue
    selectSql = """select timestamp from {0} where id = 1""".format(i[0])
    cursor.execute(selectSql)
    data = cursor.fetchall()
    if data:
        sss = """insert into increment_field (timestamp, name) value({0},'{1}')""".format(data[0][0], i[0])
        cursor.execute(sss)
        conn.commit()