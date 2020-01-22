import pandas_datareader as web
import datetime
import numpy as np
import pandas as pd
from pandas_datareader.data import Options
import matplotlib.pyplot as plt
import datetime


from pandas.plotting import scatter_matrix

start = datetime.datetime(2012,1,1)
end = datetime.datetime(2017,12,31)

tesla = web.DataReader("TSLA", 'yahoo', start, end)
ford = web.DataReader("F", 'yahoo', start, end)
generalmotor = web.DataReader("GM", 'yahoo', start, end)

# tesla['Open'].plot(figsize=(16,6),label='TSLA')
# ford['Open'].plot(figsize=(16,6),label='F')
# generalmotor['Open'].plot(figsize=(16,6),label='GM')
#
#
# tesla['Volume'].plot(figsize=(16,6),label='TSLA')
# ford['Volume'].plot(figsize=(16,6),label='F')
# generalmotor['Volume'].plot(figsize=(16,6),label='GM')
#
# print(ford['Volume'].argmax())

# tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
# ford['Total Traded'] = ford['Open'] * ford['Volume']
# generalmotor['Total Traded'] = generalmotor['Open'] * generalmotor['Volume']
#
# tesla['Total Traded'].plot(figsize=(16,6),label='TSLA')
# ford['Total Traded'].plot(figsize=(16,6),label='F')
# generalmotor['Total Traded'].plot(figsize=(16,6),label='GM')
#
# print(tesla['Total Traded'].argmax())

# generalmotor['Close'].plot(figsize=(16,6),label='GM')
# generalmotor['50days Moving'] = generalmotor.rolling(window=50).mean()['Close']
# generalmotor['200days Moving'] = generalmotor.rolling(window=200).mean()['Close']
#
#
#
# plt.legend()
# plt.show(generalmotor[['Close','50days Moving','200days Moving']].plot(figsize=(16,6)))

# df = pd.concat([tesla['Open'], ford['Open'], generalmotor['Open']], axis=1)
# df.columns = ['Tesla Open','GM Open','Ford Open']
#
# scatter_matrix(df,figsize=(3,3),alpha=0.2,hist_kwds={'bins':50})
# plt.show()


#Part 3

tesla['return'] = (tesla['Close'] / tesla['Close'].shift(1)) - 1
ford['return'] = (ford['Close'] / ford['Close'].shift(1)) - 1
generalmotor['return'] = (generalmotor['Close'] / generalmotor['Close'].shift(1)) - 1

#tesla['return'].hist(bins=50)
#ford['return'].hist(bins=50)
#generalmotor['return'].hist(bins=50)



tesla['Cumulative Return'] = (1 + tesla['return']).cumprod()
ford['Cumulative Return'] = (1 + ford['return']).cumprod()
generalmotor['Cumulative Return'] = (1 + generalmotor['return']).cumprod()

tesla['Cumulative Return'].plot(label='Tesla',figsize=(16,8),title='Cumulative Return')
ford['Cumulative Return'].plot(label='Ford')
generalmotor['Cumulative Return'].plot(label='GM')
plt.legend()

plt.show()