import json
from pyecharts.charts import Map
f = open('C:\python 程序库\地图任务\疫情.txt','r',encoding='UTF-8')
shan_dong = f.read()
f.close()
shan_dong = json.loads(shan_dong)
shan_dong = shan_dong['areaTree'][0]['children'][11]['children']
map = Map()
a = 1
data_shandong = list()
while a <= 15 :
    data_shandong.append((shan_dong[a]['name']+'市',shan_dong[a]['total']['confirm']))
    a += 1
map.add('山东疫情分布',data_shandong,'山东')
map.render('山东省.html')