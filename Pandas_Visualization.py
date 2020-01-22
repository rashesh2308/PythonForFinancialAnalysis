import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as  dates

# df1 = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/04-Visualization-Matplotlib-Pandas/04-02-Pandas Visualization/df1', index_col=0)
# print(df1.head())
# #df2 = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/04-Visualization-Matplotlib-Pandas/04-02-Pandas Visualization/df2')
# # plt.show(df['A'].hist(bins=30))
# #
# # plt.show(df['A'].plot(kind='hist' , bins=30))
#
# #plt.show(df['A'].plot.hist())
#
# #plt.show(df1.plot.scatter(x='A' , y = 'B', s= df1['C']*5))
#
# #plt.show(df1.plot.box())
#
# plt.show(df1['A'].plot.kde())

# mcd = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/04-Visualization-Matplotlib-Pandas/04-02-Pandas Visualization/mcdonalds.csv', index_col='Date', parse_dates=True)
# print(mcd.head())
#
# #plt.show(mcd['Adj. Close'].plot(xlim= ['2007-01-01', '2009-01-01'], ylim = [30,50]))
#
# idx = mcd.loc['2007-01-01':'2007-05-01'].index
#
# stock = mcd.loc['2007-01-01':'2007-05-01']['Adj. Close']
#
#
# fig,ax = plt.subplots()
# ax.plot_date(idx,stock,'-')
#
#
# # Major Axis
# ax.xaxis.set_major_locator(dates.MonthLocator())
# ax.xaxis.set_major_formatter(dates.DateFormatter('%b\n%Y'))
#
# #Minor Axis
# ax.xaxis.set_minor_locator(dates.WeekdayLocator())
# ax.xaxis.set_minor_formatter(dates.DateFormatter('%a'))
#
#
#
# #Grids
# fig.autofmt_xdate()
# ax.yaxis.grid(True)
# plt.show()


#Excercise

df3 = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/04-Visualization-Matplotlib-Pandas/04-02-Pandas Visualization/df3')
print(df3.head())


#df3.plot.scatter('b','a',s=50,figsize=(12,3))
plt.style.use('ggplot')
# df3['a'].plot.hist(alpha =0.5 , bins=20)
#
# df3[['a','b']].plot.box()
#
# df3['d'].plot.kde(ls = '--')


#Legend outside
f = plt.figure()
df3.ix[0:30].plot.area(alpha=0.4,ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))


plt.show()