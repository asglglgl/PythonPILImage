import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "STSong"
plt.rcParams["font.size"] = 20

#每份饼状图大小
a = np.arange(2.0,10.0,2,np.float)
#每份饼状图离中心点距离(大小与a的大小一致)
explode = [0,0,0,.1]
#每份饼状图的标签(大小与a的大小一致)
labels = ["饮食","交通","住宿","房贷"]
#每份饼状图的颜色 r红，b蓝,g绿，y黄
colors =  ["r","b","g","y"]
# 控制饼图内百分比设置,可以使用format字符串或者format function'%1.1f'指小数点前后位数(没有用空格补齐)
autopct = "%1.1f"
# 指定autopct的位置刻度,默认值为0.6；
pctdistance = 0.6
#是否有阴影
shadow = False
#标签的距离中心的距离 默认1.1
labeldistance = 1.1
#起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起
startangle = 90
#半径 默认1
radius = 1
#指定指针方向；布尔值，可选参数，默认为：True，即逆时针。将值改为False即可改为顺时针
counterclock = True
#字典类型，可选参数，默认值：None。参数字典传递给wedge对象用来画一个饼图。例如：wedgeprops={'linewidth':2}设置wedge线宽为2。
wedgeprops = {'linewidth':2}
# 设置标签（labels）和比例文字的格式；字典类型，可选参数，默认值为：None。传递给text对象的字典参数
textprops = None
# 饼图中心点位置
center = (0, 0)
#布尔类型，可选参数，默认值：False。如果是true，绘制带有表的轴框架
frame = True
# 布尔类型，可选参数，默认为：False。如果为True，旋转每个label到指定的角度
rotatelabels = True,

plt.pie(a,explode=[0,0,0,.1],
        labels=labels,colors=colors,
        autopct="%1.1f%%",
        labeldistance = labeldistance,
        startangle = startangle,
        radius=radius)

#设置标题
plt.title("张三的本月消费占比图")
#将饼图显示为正圆形
plt.axis('equal')

plt.legend(loc="upper right",fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)
# loc =  'upper right' 位于右上角
# bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边
# ncol=2 分两列
# borderaxespad = 0.3图例的内边距
#dpi像素点的多少 影响图片质量
plt.savefig("zhangsan.png",dpi=200)
plt.show()