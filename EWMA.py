import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

airline = pd.read_csv('/Users/rasheshkothari/Desktop/Study/Resources/Python-for-Finance-Repo-master/08-Time-Series-Analysis/airline_passengers.csv'
                      , index_col='Month')


airline.dropna(inplace=True)

airline.index = pd.to_datetime(airline.index)

airline['6months MA'] = airline['Thousands of Passengers'].rolling(window=6).mean()
airline['12months MA'] = airline['Thousands of Passengers'].rolling(window=12).mean()


airline['EWMA 12'] = airline['Thousands of Passengers'].ewm(span=12).mean()
airline['EWMA 6'] = airline['Thousands of Passengers'].ewm(span=6).mean()

airline[['Thousands of Passengers','EWMA 12', 'EWMA 6']].plot(figsize = (10,5))

#airline.plot(figsize = (10,5))
plt.show()
print(airline.head())
