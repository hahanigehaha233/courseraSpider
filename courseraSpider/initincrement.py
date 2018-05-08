import pymysql
import config
conn = pymysql.connect(host=config.MYSQL_HOST, port=3306, user=config.MYSQL_USER, passwd=config.MYSQL_PASSWD, db=config.MYSQL_DBNAME, charset='utf8')
cursor = conn.cursor()

