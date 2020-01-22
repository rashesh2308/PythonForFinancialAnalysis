from scipy import stats
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt


start = pd.to_datetime('2017-01-01')
end = pd.to_datetime('2019-12-31')

orcl = web.DataReader('ORCL', 'yahoo', start, end)
spy_etf = web.DataReader('SPY','yahoo',start, end)
print(spy_etf.head())


print(orcl.head())
#orcl['Close'].plot(label='ORACLE')
#spy_etf['Close'].plot(label = 'SPY')
#
# plt.legend()
# plt.show()

orcl['Cumulative'] = orcl['Close'] / orcl['Close'].iloc[0]
spy_etf['Cumulative'] = spy_etf['Close'] / spy_etf['Close'].iloc[0]
#
# orcl['Cumulative'].plot(label='ORACLE')
# spy_etf['Cumulative'].plot(label = 'SPY')

orcl['Daily Return'] = orcl['Close'].pct_change(1)
spy_etf['Daily Return'] = spy_etf['Close'].pct_change(1)

#plt.scatter(orcl['Daily Return'],spy_etf['Daily Return'],alpha=0.25 )

beta,alpha,r_value,p_value,std_err = stats.linregress(orcl['Daily Return'].iloc[1:],
                                                      spy_etf['Daily Return'].iloc[1:])

print("beta: ", beta, "alpha: " , alpha)

noise = np.random.normal(0,0.001,len(spy_etf['Daily Return'].iloc[1:]))
# print("Noise: " , noise)

fake_noise = spy_etf['Daily Return'].iloc[1:] + noise
plt.scatter(fake_noise, spy_etf['Daily Return'].iloc[1:], alpha=0.25)


plt.legend()
plt.show()
