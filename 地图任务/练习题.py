import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts
from pyecharts.options import VisualMapOpts
from pyecharts.options import LabelOpts
f = open('C:\python 程序库\地图任务\疫情.txt','r',encoding='UTF-8')
data_all = f.read()
data_all = json.loads(data_all)
data = data_all['areaTree'][0]['children']
a = 0
enta_ = list()
while(a <= 33):
    if data[a]['name'] == '香港' or data[a]['name'] == '澳门':
        enta_.append((data[a]['name'] + '特别行政区', data[a]['total']['confirm']))
    elif data[a]['name'] == '北京' or data[a]['name'] == '天津' or data[a]['name'] == '上海' or data[a]['name'] == '重庆' :
        enta_.append((data[a]['name'] + '市', data[a]['total']['confirm']))
    elif data[a]['name'] == '内蒙古' or data[a]['name'] == '西藏':
        enta_.append((data[a]['name'] + '自治区', data[a]['total']['confirm']))
    elif data[a]['name'] == '广西':
        enta_.append((data[a]['name'] + '壮族自治区', data[a]['total']['confirm']))
    elif data[a]['name'] == '新疆':
        enta_.append((data[a]['name'] + '维吾尔自治区', data[a]['total']['confirm']))
    elif data[a]['name'] == '宁夏':
        enta_.append((data[a]['name'] + '回族自治区', data[a]['total']['confirm']))
    else:
        enta_.append((data[a]['name']+'省',data[a]['total']['confirm']))
    a += 1
map = Map()
map.add('作业地图',enta_,'china',label_opts=LabelOpts(is_show=False))
map.set_global_opts(
    title_opts=TitleOpts(title='全国疫情地图',pos_right='center',pos_bottom='1px'),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, 'max': 99, 'lable': '1-99人', 'color': '#cff'},
            {'min': 100, 'max': 999, 'lable': '100-999人', 'color': '#ff9'},
            {'min': 1000, 'max': 4999, 'lable': '1000-4999人', 'color': '#f96'},
            {'min': 5000, 'max': 9999, 'lable': '5000-9999人', 'color': '#f66'},
            {'min': 10000, 'max': 99999, 'lable': '10000-99999人', 'color': '#c33'},
            {'min': 100000, 'lable': '100000以上', 'color': '#903'},
        ]
    )
)
map.render('全国疫情.html')