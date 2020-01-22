import pandas_datareader as web
import datetime
import numpy as np
import pandas as pd
from pandas_datareader.data import Options
import matplotlib.pyplot as plt
from datetime import datetime
import quandl
quandl.ApiConfig.api_key = 'VYsf7X4RBp3sgNRYCB61'

# start = datetime.datetime(2015,1,1)
# end = datetime.datetime(2017,12,31)
#
# facebook = web.DataReader("FB", 'yahoo', start, end)
# print(facebook.head())
#
#
# fb_options = Options('FB', 'yahoo')
# data = fb_options.get_options_data(expiry=fb_options.expiry_dates[0])
#
# print(data.head())
#
# my_data = quandl.get("WIKI/AAPL")
# print(my_data.columns)


#RESAMPLING
#
# df = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/05-Pandas-with-Time-Series/time_data/walmart_stock.csv')
#
#
# #careating date as index
#
# df['Date'] = df['Date'].apply(pd.to_datetime)
# df.set_index('Date',inplace=True)
# print(df.head())
#
# #OR
#
# #df = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/05-Pandas-with-Time-Series/time_data/walmart_stock.csv',
# #                 index_col='Date', parse_dates=True)
#/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/
# print(df.resample(rule='BQ').mean())
#
# plt.show(df['Close'].resample('A').mean().plot(kind='bar'))
#

#TIME-SHIFT

df = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/05-Pandas-with-Time-Series/time_data/walmart_stock.csv',
               index_col='Date', parse_dates=True)

#print(df.shift(periods=1).head())
#^Shifts down

#df.tshift(freq='M').head()

df['Open'].plot(figsize = (16,6))
df['20days Moving'] = df.rolling(window=20).mean()['Close']
df['Upper BB'] = df['20days Moving'] + 2 * (df['Close'].rolling(window=20).std())
df['Lower BB'] = df['20days Moving'] - 2 * (df['Close'].rolling(window=20).std())


plt.show(df[['Open' , '20days Moving', 'Upper BB', 'Lower BB']].plot(figsize=(16,6)))