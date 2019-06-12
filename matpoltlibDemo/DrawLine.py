import matplotlib.pyplot as plt
import matplotlib
import numpy as np
#
# # 坐标轴支持中文
# # matplotlib.rcParams["font.family"] = "STSong"
# # matplotlib.rcParams["font.size"] = 20
#
# # 画线
a = np.arange(0.0,5.0,0.02)
#将画布分为2行一列在第一块的位置
plt.subplot(211)
plt.plot(a,np.cos(a*np.pi*2),'b-.')

b = np.random.normal(2,5,10)
plt.subplot(212)
#r-- 表示红色的--线
plt.plot(b,'r--')
plt.show()