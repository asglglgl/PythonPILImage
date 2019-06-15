'''
绘制直方图
'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import mlab

#数据去一维正态分布
mu = 3
sigma =0.1
x= np.random.normal(mu,sigma,1000)
'''
x,  x轴数据
bins=None 整数或数组 条形图个数
range=None,范围
density=None,是否以密度的形式显示
weights=None,
cumulative=False,
bottom=None,
histtype='bar',线条类型 bar":方形，"barstacked":柱形,"step":"未填充线条""stepfilled":"填充线条"
align='mid', 对齐方式 left，mid，right
orientation='vertical', "horizontal":水平，"vertical":垂直
rwidth=None,
log=False,单位是否以科学计术法
color=None,指定条状图的颜色
label=None,
stacked=False,
normed=None,密度,也就是每个条状图的占比例比,默认为1 
'''
n ,n_bins,patches=plt.hist(x,100,density=1,facecolor= 'b')

y = mlab.normpdf(n_bins, mu, sigma)
plt.plot(n_bins,y,'r--')
plt.xlabel('x轴',fontproperties = "SimHei")
plt.ylabel('y轴',fontproperties="SimHei")
plt.title(r'正态分布 : $\mu=3$, $\sigma=0.1$',fontproperties="SimHei")
plt.subplots_adjust(left=0.15)
plt.show()