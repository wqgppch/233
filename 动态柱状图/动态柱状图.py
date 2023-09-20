from pyecharts.charts import Bar
from pyecharts.charts import Timeline
from pyecharts.options import LabelOpts,TitleOpts
from pyecharts.globals import ThemeType
data_f = open('C:\python 程序库\动态柱状图/1960-2019全球GDP数据.csv','r',encoding='GB2312')
data = data_f.readlines()
del data[0]
data_dict ={}
for a in data:
    year = int(a.split(',')[0])
    country = a.split(',')[1]
    GDP = float(a.split(',')[2])
    try:
        data_dict[year].append([country,GDP])
    except KeyError :
        data_dict[year] = []
        data_dict[year].append([country,GDP])
key = sorted(data_dict.keys())
timeBAR = Timeline(
    {'theme':ThemeType.LIGHT}
)
for a in key:
    data_dict[a].sort(key=lambda s:s[1],reverse=True)
    year_data = data_dict[a][0:8]
    x_data = list()
    y_data = list()
    for d in year_data:
        x_data.append(d[0])
        y_data.append(int(d[1]/100000000))
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GTP',y_data,label_opts=LabelOpts(position='right'))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{a}年的GPT数据")
    )
    timeBAR.add(bar,str(a))
timeBAR.add_schema(
    is_timeline_show=True,
    play_interval=1000,
    is_auto_play=True,
)
timeBAR.render()