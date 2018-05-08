import pymysql
import config
conn = pymysql.connect(host=config.MYSQL_HOST, port=3306, user=config.MYSQL_USER, passwd=config.MYSQL_PASSWD, db=config.MYSQL_DBNAME, charset='utf8')
cursor = conn.cursor()
try:
    sql = """show tables;"""
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        if i[0] in ('project', 'id', 'sub_href', 'increment'):
            continue
        findMaxSql = """select max(timestamp) timestamp from {0}""".format(i[0])
        cursor.execute(findMaxSql)
        data = cursor.fetchall()
        updateSql = """update increment_field set timestamp = '{0}' where name = '{1}'""".format(data[0][0], i[0])
        cursor.execute(updateSql)
        conn.commit()
        print i[0]+' Done'
except Exception as error:
    print error