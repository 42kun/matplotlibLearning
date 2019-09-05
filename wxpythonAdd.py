import wx
from matplotlib.backends import backend_wxagg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS','SimHei']
plt.rcParams['axes.unicode_minus'] = False

"""
https://www.wxpython.org/Phoenix/docs/html/wx.GridBagSizer.html#wx-gridbagsizer
https://www.wxpython.org/Phoenix/docs/html/wx.FlexGridSizer.html#wx.FlexGridSizer.AddGrowableCol
"""
class TestFrame(wx.Frame):
    #初始化各元素
    def __init__(self):
        wx.Frame.__init__(self,None,title = "测试程序")
        self.SetBackgroundColour("White")
        self.AddMainElements()

    #添加顶级元素
    def AddMainElements(self):
        self.titlePanel = self.AddTitlePanel()
        self.graphPanel = graphPanel(self)
        self.numberPanel = self.AddNumberPanel()

        sizer = wx.GridBagSizer(10,5) #设置格子横竖边距


    #生成标题面板
    def AddTitlePanel(self):
        #TODO:居中问题有待解决
        titlePanel = wx.Panel(self,name="titlePanel")
        titlePanel.SetBackgroundColour("yellow") #TODO:带调试完成后删除此句
        title = wx.StaticText(titlePanel,label = "matplotlib嵌入wxpython演示",name = "title")
        titleFont = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD) #设置字体
        title.SetFont(titleFont)
        return titlePanel

    def AddNumberPanel(self):
        numberPanel  = wx.Panel(self,name="numberPanel")
        xText = wx.StaticText(numberPanel,label = "x",name = "xText")
        xCtrl = wx.TextCtrl(numberPanel,style =  wx.TE_READONLY,name = "xCtrl")
        yText = wx.StaticText(numberPanel, label="y",name = "yText")
        yCtrl = wx.TextCtrl(numberPanel, style=wx.TE_READONLY ,name = "yCtrl")
        return numberPanel

#生成图像面板
class graphPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.matplotlibPanel = backend_wxagg.FigureCanvasWxAgg(self, -1, Figure())
        self.drawGraph()

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

#TODO 完成底部数值面板
#TODO 获取数值
#TODO 解决大小问题（理想情况下大小等块最好）
#TODO 添加虚线与焦点数值

if __name__ == "__main__":
    app = wx.App()
    win = TestFrame()
    win.Show()
    app.MainLoop()