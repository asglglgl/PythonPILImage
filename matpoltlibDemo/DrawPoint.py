import matplotlib.pyplot as plt
#scatter 第一个参数为x轴坐标，第二个参数为y轴坐标
plt.scatter((1,2,3,4,5),(1,2,3,4,5),c = "red")
#fontproperties参数是为了中文显示
plt.ylabel("y轴",fontproperties = "Simhei",fontsize = "20")
plt.xlabel("x轴",fontproperties = "Simhei",fontsize = "20")
plt.show()