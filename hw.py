import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False	
data = pd.read_csv(".\covid19_data.csv")
xdata =[]
xdata = data.loc[:,'發病年週']
line1 = data.loc[:,'確定病例']
line2 = data.loc[:,'通報病例']
week = range(0,42)
plt.title("410xxxxxxxx")
plt.xticks(week,xdata)
plt.plot(line1,"y",label = '確定病例',linewidth=1)
plt.plot(line2,"black",label = '通報病例',linewidth=1)
plt.legend()
plt.xlabel('發病年週')
plt.ylabel('人數')
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()

#確定病例
#通報病例