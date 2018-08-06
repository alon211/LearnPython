import matplotlib.pyplot as pt
import pandas as pd
#防止中文乱码。。。
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
x=[1,3,4,5,6,7]
y=[5,-2,-3,4,-6,-7]
data = pd.read_excel("201708071517.xls")
data=data.head(50)

#显示子图表
#首先需要创建一个figure对象
fig=pt.figure()
#创建你的图标,subplots参数分别代表2行2列第3个
graph1=fig.add_subplot(2,2,3)
graph1.plot(x,y)


