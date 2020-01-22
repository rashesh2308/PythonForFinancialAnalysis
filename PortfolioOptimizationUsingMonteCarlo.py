import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import quandl
quandl.ApiConfig.api_key = 'VYsf7X4RBp3sgNRYCB61'
from pprint import pprint
np.random.seed(101)

start = pd.to_datetime('2017-01-01')
end = pd.to_datetime('2019-12-31')
#
orcl = quandl.get('WIKI/ORCL.11',start_date=start,end_date=end)
ms = quandl.get('WIKI/MS.11',start_date=start,end_date=end)
pfe = quandl.get('WIKI/PFE.11',start_date=start,end_date=end)
ford = quandl.get('WIKI/F.11',start_date=start,end_date=end)

stocks = pd.concat([orcl,ms,pfe,ford],axis=1)
stocks.columns = ['ORCL', 'MS' , 'PFE', 'FORD']

#print("Normal return: \n", stocks.pct_change(1).head())
#print(stocks.pct_change(1).corr())

# log_return = np.log(stocks/stocks.shift(1))
# #print("Log returns: \n" , log_return.head())
#
# #print("Annual Covariance: " , log_return.cov() *252)
#
# print(stocks.columns)
# weight = np.array(np.random.random(4))
# #making sure that sum is 1
# print("Random weights: ", weight/np.sum(weight))
#
# #Expected portfolio Return
# expected_return = np.sum(log_return.mean() * weight * 252)
# print("Expected return (Rp):", expected_return)
#
# #Expected volatility
# expected_volatility = exp_vol = np.sqrt(np.dot(weight.T, np.dot(log_return.cov() * 252, weight)))
# print("Expected Volatility (Sp):", expected_volatility)
#
# #Sharp Ratio
# sharp_ratio = expected_return / expected_volatility
# print("Sharp Ratio:", sharp_ratio)

num_ports = 500

all_weights = np.zeros((num_ports, len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)
log_return = np.log(stocks/stocks.shift(1))


for ind in range(num_ports):
    # Create Random Weights
    weights = np.array(np.random.random(4))

    # Rebalance Weights
    weights = weights / np.sum(weights)

    # Save Weights
    all_weights[ind, :] = weights

    # Expected Return
    ret_arr[ind] = np.sum((log_return.mean() * weights) * 252)

    # Expected Variance
    vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_return.cov() * 252, weights)))

    # Sharpe Ratio
    sharpe_arr[ind] = ret_arr[ind] / vol_arr[ind]


print(sharpe_arr.max())
print(sharpe_arr.argmax())

max_sr_ret = ret_arr[285]
max_sr_vol = vol_arr[285]

plt.figure(figsize=(12,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

# Add red dot for max SR
plt.scatter(max_sr_vol,max_sr_ret,c='red',s=50,edgecolors='black')

plt.show()


#MATHAMATICS OPTIMIZATION

