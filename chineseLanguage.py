import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS','SimHei']
# plt.rcParams['axes.unicode_minus'] = False

x = np.arange(1,10,0.5)
y = 0.5**x

plt.yscale("log")
plt.title("中文测试")
plt.plot(x,y)
plt.show()