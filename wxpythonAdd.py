import wx
from matplotlib.backends import backend_wxagg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS','SimHei']
plt.rcParams['axes.unicode_minus'] = False

class TestFrame(wx.Frame):
    #初始化各元素
    def __init__(self):
        wx.Frame.__init__(self,None,title = "测试程序")
        self.SetBackgroundColour("White")

        self.titlePanel = self.AddTitlePanel()
        self.graphPanel = graphPanel(self)

        #设置GridBadSize尺寸器行列间隙
        sizer = wx.GridBagSizer(5,15)

        #将标题面板添加入尺寸器
        self.titlePanel.SetMinSize((600,80))
        sizer.Add(self.titlePanel,(0,0),(0,4),wx.EXPAND)
        sizer.AddGrowableCol(0)
        # sizer.AddGrowableCol(1)
        # sizer.AddGrowableCol(2)
        # sizer.AddGrowableCol(3)

        #将图像面板添加入尺寸器
        self.graphPanel.SetMinSize((600,350))
        sizer.Add(self.graphPanel,(1,0),(3,4),wx.EXPAND)
        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(3)

        #为Frame添加尺寸器，并根据组件大小适配Frame大小
        self.SetSizerAndFit(sizer)

        self.Center()




    #生成标题面板
    def AddTitlePanel(self):
        titlePanel = wx.Panel(self,name="titlePanel")
        title = wx.StaticText(titlePanel,label = "matplotlib嵌入wxpython演示",name = "title")
        titleFont = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD) #设置字体
        title.SetFont(titleFont)

        #设置标题居中（方法出自https://stackoverflow.com/questions/20737965/wxpython-how-do-i-center-a-static-size-panel）
        sizer = wx.BoxSizer()
        sizer.AddStretchSpacer(1)
        sizer.Add(title,flag = wx.ALIGN_CENTER)
        sizer.AddStretchSpacer(1)
        titlePanel.SetSizer(sizer)

        return titlePanel

#生成图像面板
class graphPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        """self.matplotlibPanel完全继承自wx.Panel类，可以与Panel类一样的使用"""
        self.matplotlibPanel = backend_wxagg.FigureCanvasWxAgg(self, -1, Figure())
        self.drawGraph()

        sizer = wx.BoxSizer()
        sizer.AddStretchSpacer(1)
        sizer.Add(self.matplotlibPanel,flag = wx.EXPAND)
        sizer.AddStretchSpacer(1)
        self.SetSizer(sizer)

    #绘制函数图像
    def drawGraph(self):
        #获取figure
        fig = self.matplotlibPanel.figure

        x = np.arange(1,5,0.1)
        y1 = np.log(x)
        y2 = x**2-4*x+1

        axes1 = fig.add_subplot(121)
        axes1.set_xlabel("x")
        axes1.set_ylabel("y")
        axes1.plot(x,y1,color="blue")

        axes2 = fig.add_subplot(122)
        axes2.set_xlabel("x")
        axes2.set_ylabel("y")
        axes2.plot(x, y2,color="orange")

        fig.suptitle("简单函数图像")


if __name__ == "__main__":
    app = wx.App()
    win = TestFrame()
    win.Show()
    app.MainLoop()