"""
随机绘制CIFAR-10内部的一些数据
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import pickle

#处理中文
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS','SimHei']

#获取文件路径
dir = os.path.join(*["cifar10DrawData","data_batch_1"])

"""获得图像数据并转换为matplotlib所需要的格式"""
with open(dir,'rb') as fp:
    t = pickle.load(fp,encoding='bytes') #将文件反序列化，还原为python字典
    data = np.array(t[b'data']) #获取图片数据 10000*3072
    labels = np.array(t[b'labels']) #获取标签 10000
    data = data.reshape((-1, 3, 32, 32)) #将data转换为三维数组，形状为 10000*3*32*32
    data = data.transpose(0,2,3,1) #将data转换为matplotlib所能绘制的形式


"""每种图像收集10张，存到img数组中"""
img = [[] for i in range(10)] #用来保存所需要的图像对应的位置

sum = p = 0 #sum保存存储的图像总张数，p保存读取的图像位置
while sum<100:
    if len(img[labels[p]])<10:
        img[labels[p]].append(p)
        sum+=1
    p+=1


"""准备绘图"""
cols = [str(i) for i in range(10)] #列标签
rows = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'] # 行标签

fig,axes = plt.subplots(10,10,figsize = (8,8)) #创建10*10的子图，每个子图大小为8*8
for ax,col in zip(axes[0],cols): #设置列标签
    ax.set_title(col)

for ax,row in zip(axes[:,0],rows): #设置行标签
    ax.set_ylabel(row,rotation=0,fontsize="x-small",ha="right")

for i in range(10):
    for j in range(10):
        axes[i,j].imshow(data[img[i][j]]) #绘制图像
        axes[i, j].set_xticks([]) #关闭坐标
        axes[i, j].set_yticks([])
        # axes[i,j].axis('off') #不能使用这一句，它会使行标签消失

plt.suptitle("绘制CIFAR10")
plt.show()