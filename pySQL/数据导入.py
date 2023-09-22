import json
from pymysql import Connection
class Record :

    '''
    数据封装
    '''

    def __init__(self,date,order_id,money,province):
        self.date = date
        self.order_id = order_id
        self.money : int  = int(money)
        self.province = province

    def __str__(self):
        return f'{self.date},{self.order_id},{self.money},{self.province}'

class FileRead :

    '''
    父类
    '''

    def read_data(self) -> list[Record]:
        pass

class TxtFileRead (FileRead) :

    '''
    传入文件路径，导出包含类对象的列表
    '''

    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path,'r',encoding='UTF-8')
        record_list = []
        for line in f.readlines() :
            line = line.strip().split(',')
            record = Record(line[0],line[1],line[2],line[3])
            record_list.append(record)
        f.close()
        return record_list
class JsonFileRead (FileRead) :

    '''
    传入文件路径，导出包含类对象的列表
    '''

    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path,'r',encoding='UTF-8')
        record_list = []
        for line in f.readlines() :
            line_dict = json.loads(line.strip())
            record = Record(line_dict['date'],line_dict['order_id'],line_dict['money'],line_dict['province'])
            record_list.append(record)
        f.close()
        return record_list

txt_read = TxtFileRead('C:\python 程序库\pySQL\TXT.txt')
json_read = JsonFileRead('C:\python 程序库\pySQL\Json.txt')
txt_list = txt_read.read_data()         # type: list[Record]
json_list = json_read.read_data()       # type: list[Record]

all_list = txt_list + json_list         # type: list[Record]

"""
链接数据库
"""
con = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)

'''
建立游标对象
'''
con_cur = con.cursor()

con_cur.execute('create database 测试')

con.select_db('测试')
con_cur.execute("create table 测试表格 (date1		varchar(15),order_id	varchar(100),money		int,province	varchar(10))")
for a in all_list:
    sql = f"insert into 测试表格 values ('{a.date}','{a.order_id}',{a.money},'{a.province}')"
    con_cur.execute(sql)

