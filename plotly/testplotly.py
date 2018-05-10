import plotly.plotly
from plotly.graph_objs import *
import pymysql
import courseraSpider.config
import datetime
conn = pymysql.connect(host=courseraSpider.config.MYSQL_HOST, port=3306, user=courseraSpider.config.MYSQL_USER,
                       passwd=courseraSpider.config.MYSQL_PASSWD, db=courseraSpider.config.MYSQL_DBNAME, charset='utf8')
cursor = conn.cursor()
sql1 = """ select timestamp from big_data_introduction"""
sql2 = """select timestamp from big_data_management"""
sql3 = """select timestamp from big_data_integration_processing"""
sql4 = """select timestamp from big_data_machine_learning"""
cursor.execute(sql1)
result1 = cursor.fetchall()
data1 = []
cursor.execute(sql2)
result2 = cursor.fetchall()
data2 = []
cursor.execute(sql3)
result3 = cursor.fetchall()
data3 = []
cursor.execute(sql4)
result4 = cursor.fetchall()
data4 = []
for i in result1:
    data1.append(datetime.datetime.fromtimestamp(float(i[0])).date().isocalendar())
for i in result2:
    data2.append(datetime.datetime.fromtimestamp(float(i[0])).date().isocalendar())
for i in result3:
    data3.append(datetime.datetime.fromtimestamp(float(i[0])).date().isocalendar())
for i in result4:
    data4.append(datetime.datetime.fromtimestamp(float(i[0])).date().isocalendar())
num1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in data1:
    num1[i[2]] = num1[i[2]] + 1
for i in data2:
    num2[i[2]] = num2[i[2]] + 1
for i in data3:
    num3[i[2]] = num3[i[2]] + 1
for i in data4:
    num4[i[2]] = num4[i[2]] + 1

big_data_introduction = Scatter(
    y=num1,
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    name='big_data_introduction'
)
big_data_management = Scatter(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y=num2,
    name='big_data_management'
)
big_data_integration_processing = Scatter(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y=num3,
    name='big_data_integration_processing'
)
big_data_machine_learning = Scatter(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y=num4,
    name='big_data_machine_learning'
)
data = Data([big_data_introduction, big_data_management, big_data_integration_processing, big_data_machine_learning])
#
plotly.offline.plot(data, filename='test1.html')