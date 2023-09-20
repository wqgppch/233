from pyecharts.charts import Map
from pyecharts.options import TitleOpts
from pyecharts.options import VisualMapOpts
map = Map()
map.set_global_opts(
    title_opts=TitleOpts(title='山河四省',pos_right='center',pos_bottom='1px'),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, 'max': 5, 'label': '山东省', 'color': '#000'},
            {'min': 6, 'max': 10, 'label': '河北省', 'color': '#f00'},
            {'min': 11, 'max': 15, 'label': '山西省', 'color': '#0f0'},
            {'min': 16, 'max': 20, 'label': '河南省', 'color': '#00f'},
        ]
    )
)
data = [('山东省',5),('河北省',10),('山西省',15),('河南省',20),]
map.add('测试地图',data,'china')
map.render()