# -*- coding: utf-8 -*-
"""
绘制柱状图
"""

import matplotlib.pyplot as plt
import numpy as np

# 数据数目
n = 10
x = np.arange(n)
# 生成数据, 均匀分布(0.5, 1.0)之间
y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)



# x 横坐标的值
# height 高度 纵坐标的值
# width = 0.8 柱状图宽度
# bottom = None
# align = 'center' 可选['left'(default) | 'center']决定整个bar图分布 默认left表示默认从左边界开始绘制,center会将图绘制在中间位置
# edgecolor 边界颜色
#color 柱状图颜色

# 绘制柱状图, 向上
plt.bar(x, y1, color = 'blue', edgecolor = 'white')
# 绘制柱状图, 向下
plt.bar(x, -y2, color = 'red', edgecolor = 'white')

#zip函数会将x,y打包为（（x1,y1）,(x2,y2)...(xn,yn)）
temp = zip(x, y2)
# 在柱状图上显示具体数值, ha水平对齐, va垂直对齐
for x, y in zip(x, y1):
    # 第一个和第二个参数 描述显示的位置，第三个参数为显示的内容
    plt.text(x + 0.05, y + 0.1, '%.2f' % y, ha = 'center', va = 'bottom')

for x, y in temp:
    plt.text(x + 0.05, -y - 0.1, '%.2f' % y, ha = 'center', va = 'bottom')

# 设置坐标轴范围
plt.xlim(-1, n)
plt.ylim(-1.5, 1.5)

plt.title("这是标题",fontproperties = "Simhei",fontsize = "20")
# 去除坐标轴
plt.xticks(())
plt.yticks(())
plt.savefig("ColumnsChart")
plt.show()
