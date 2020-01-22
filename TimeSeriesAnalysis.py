import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = sm.datasets.macrodata.load_pandas().data
print(sm.datasets.macrodata.NOTE)


index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1','2009Q3'))
df.index  = index
print(df.head())


gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df.realgdp)
df["trend"] = gdp_trend

df[['trend','realgdp']].plot()
plt.show()
