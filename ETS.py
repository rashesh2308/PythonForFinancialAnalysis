import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

airline = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/08-Time-Series-Analysis/airline_passengers.csv'
                      , index_col='Month')

print(airline.head())

#plt.show(airline.plot())

airline.dropna(inplace=True)

airline.index = pd.to_datetime(airline.index)

#print(airline.head())

result = seasonal_decompose(airline['Thousands of Passengers'], model='additive')
result2 = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')

result.plot()
result2.trend.plot(color = 'r',alpha = 0.5)

plt.show()
