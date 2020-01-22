import pandas as pd
import matplotlib.pyplot as plt
import quandl
quandl.ApiConfig.api_key = 'VYsf7X4RBp3sgNRYCB61'
from pprint import pprint

start = pd.to_datetime('2017-01-01')
end = pd.to_datetime('2019-12-31')

orcl = quandl.get('WIKI/ORCL.11',start_date=start,end_date=end)
ms = quandl.get('WIKI/MS.11',start_date=start,end_date=end)
pfe = quandl.get('WIKI/PFE.11',start_date=start,end_date=end)
ford = quandl.get('WIKI/F.11',start_date=start,end_date=end)

for stock_df in (orcl,ms,pfe,ford):
    stock_df['Normed Return'] = stock_df['Adj. Close']/stock_df.iloc[0]['Adj. Close']

for stock_df,allo in zip([orcl,ms,pfe,ford],[.1,.1,.4,.1]):
    stock_df['Allocation'] = stock_df['Normed Return']*allo

for stock_df in [orcl,ms,pfe,ford]:
    stock_df['Position Values'] = stock_df['Allocation']*500

portfolio_val = pd.concat([orcl['Position Values'],ms['Position Values'],pfe['Position Values'],ford['Position Values']],axis=1)
portfolio_val.columns = ['ORCL Pos','MS Pos','UBER Pos','FORD Pos']

portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)

# portfolio_val['Total Pos'].plot(figsize=(10,8))
# plt.title('Total Portfolio Value')
#
# portfolio_val.drop('Total Pos', axis = 1).plot(figsize=(10,8))
# plt.title('Portfolio Value by stocks')
#


portfolio_val['Daily return'] = portfolio_val['Total Pos'].pct_change(1)

print("Mean: ",portfolio_val['Daily return'].mean())
print("Standard Deviation: ",portfolio_val['Daily return'].std())

portfolio_val['Daily return'].hist(bins=100)


cumm_return = 100 * ((portfolio_val['Total Pos'][-1] / portfolio_val['Total Pos'][0]) -1)

print('cumm_return: ', cumm_return)

sharp_ratio = portfolio_val['Daily return'].mean() / portfolio_val['Daily return'].std()

annual_sharp_ratio = sharp_ratio * (252 ** 0.5)

print("Sharp Ratio (Annual): " , annual_sharp_ratio)

print(portfolio_val.head())


#plt.show()
