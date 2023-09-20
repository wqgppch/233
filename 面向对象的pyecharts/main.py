import json

from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

class Record :

    def __init__(self,date,order_id,money,province):
        self.date = date
        self.order_id = order_id
        self.money : int  = int(money)
        self.province = province

    def __str__(self):
        return f'{self.date},{self.order_id},{self.money},{self.province}'

class FileRead :

    def read_data(self) -> list[Record]:
        pass

class TxtFileRead (FileRead) :

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

txt_read = TxtFileRead('C:\python 程序库\类\TXT.txt')
json_read = JsonFileRead('C:\python 程序库\类\Json.txt')
txt_list = txt_read.read_data()         # type: list[Record]
json_list = json_read.read_data()       # type: list[Record]

all_list = txt_list + json_list         # type: list[Record]

money_dict = {}
for record in all_list :
    if record.date in money_dict :
        money_dict[record.date] += record.money
    else:
        money_dict[record.date] = record.money

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.add_xaxis(list(money_dict.keys()))
bar.add_yaxis('销售额' , list(money_dict.values()),label_opts=LabelOpts(is_show=False))
bar.render("每日销售额.html")