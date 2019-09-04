"""
本程序简单记录单幅图的一些常规操作
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS','SimHei']
plt.rcParams['axes.unicode_minus'] = False

#生成x
x = np.arange(-1,1,0.01)
#生成y1
y1 = x**5-x
#生成y2
y2 = x**3-x

#设定x轴，y轴标签
plt.xlabel("x值")
plt.ylabel("y值")

#设定x轴，y轴范围
plt.xlim(-2,2)
plt.ylim(-1,1)
#等效于
#plt.axis([-2,2,-1,1])

#设置x轴，y轴刻度(精度)
plt.xticks(np.arange(-1,1,0.1))

#设定图片名称
plt.title("方程绘制")

#绘制图像(同时设置图例，通过label标签)
plt.plot(x,y1,label = "五次方程")
plt.plot(x,y2,label = "三次方程",color='red', linewidth=2.0, linestyle='--')

#标注一个点
plt.annotate("这是零点",#标示文字
             (0,0),#文字位置
             xytext = (20,-20),#位置偏差值
             textcoords = 'offset points',#相对于原点偏差
             arrowprops = {'arrowstyle':'->'}#绘制箭头
             )
#显示图例
plt.legend()

#绘制图表
plt.show()


