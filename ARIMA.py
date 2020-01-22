import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from pprint import pprint
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from pandas.tseries.offsets import DateOffset

df = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/08-Time-Series-Analysis/monthly-milk-production-pounds-p.csv')

df.columns = ['Month' , 'Milk pound per cow']
df.drop(168, axis=0, inplace=True)

df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True )

col = df['Milk pound per cow']

df['mean 12'] = col.rolling(12).mean()
df['std 12'] = col.rolling(12).std()

# df['mean 12'].plot(label='12 mean')
# df['std 12'].plot(label='12 std')


result = seasonal_decompose(col, model='additive')
result2 = seasonal_decompose(col, model='multiplicative')

# result.plot()
# result2.trend.plot(color = 'r',alpha = 0.5)


resultx = adfuller(df['Milk pound per cow'])


def adf_check(time_series):
    """
    Pass in a time series, returns ADF report
    """
    result = adfuller(time_series)
    print('Augmented Dickey-Fuller Test:')
    labels = ['ADF Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used']

    for value, label in zip(result, labels):
        print(label + ' : ' + str(value))

    if result[1] <= 0.05:
        print(
            "strong evidence against the null hypothesis, reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")

#adf_check(df['Milk pound per cow'])
#pprint.pprint(resultx)




df['First difference'] = df['Milk pound per cow'] - df['Milk pound per cow'].shift(1)
df['First difference'].plot()


df['Second difference'] = df['First difference'] - df['Milk pound per cow'].shift(1)
adf_check(df['First difference'].dropna())
#adf_check(df['Second difference'].dropna())



df['Seasonal First Difference'] = df['First difference'] - df['First difference'].shift(12)
df['Seasonal First Difference'].plot()

adf_check(df['Seasonal First Difference'].dropna())



plot_acf(df["Seasonal First Difference"].dropna())
plot_pacf(df["Seasonal First Difference"].dropna())



model = sm.tsa.statespace.SARIMAX(df['Milk pound per cow'],order=(0,1,0), seasonal_order=(1,1,1,12))
resultmodel = model.fit()

df['predictions'] = resultmodel.predict(start=140, end=168)

df[['Milk pound per cow','predictions']].plot()


future_dates = [df.index[-1] + DateOffset(months=x) for x in range(0,24)]
future_dates_df = pd.DataFrame(index=future_dates[1:],columns=df.columns)

final_df = pd.concat([df,future_dates_df])

final_df['forecast'] = resultmodel.predict(start = 168, end = 188, dynamic= True)

final_df[['Milk pound per cow', 'forecast']].plot(figsize=(12, 8))

print(future_dates_df)
# plt.show()
# pprint(resultmodel.summary())

plt.show()