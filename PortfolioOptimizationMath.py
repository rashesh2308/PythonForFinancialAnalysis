import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import quandl
quandl.ApiConfig.api_key = 'VYsf7X4RBp3sgNRYCB61'
from scipy.optimize import minimize

np.random.seed(101)

start = pd.to_datetime('2017-01-01')
end = pd.to_datetime('2019-12-31')

orcl = quandl.get('WIKI/ORCL.11',start_date=start,end_date=end)
ms = quandl.get('WIKI/MS.11',start_date=start,end_date=end)
pfe = quandl.get('WIKI/PFE.11',start_date=start,end_date=end)
ford = quandl.get('WIKI/F.11',start_date=start,end_date=end)

stocks = pd.concat([orcl,ms,pfe,ford],axis=1)
stocks.columns = ['ORCL', 'MS' , 'PFE', 'FORD']


num_ports = 100
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

#print('vol_arr',vol_arr)

def get_ret_vol_sr(weights):
    """
    Takes in weights, returns array or return,volatility, sharpe ratio
    """
    weights = np.array(weights)
    ret = np.sum(log_return.mean() * weights) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_return.cov() * 252, weights)))
    sr = ret/vol
    return np.array([ret,vol,sr])

def negative_sharp(weights):
    return get_ret_vol_sr(weights)[2] * -1

def check_sum(weights):
    return np.sum(weights) - 1


constraints = ({'type': 'eq' , 'fun' : check_sum})
bounds = ((0,1),(0,1),(0,1),(0,1))
initial_guess = [0.25,0.25,0.25,0.25]

optimization_function = minimize(negative_sharp, initial_guess,bounds=bounds, constraints=constraints, method= 'SLSQP')
#rint(optimization_function.x)


print("return volatility and SR", get_ret_vol_sr(optimization_function.x))

#All Optimal Portfolios (Efficient Frontier)

frontier_y = np.linspace(0,0.3,500)

def min_vol(weights):
    return  get_ret_vol_sr(weights)[1]

frontier_vol = []

for possible_return in frontier_y:
    cons = ({'type':'eq', 'fun' : check_sum},
            {'type':'eq' ,'fun' : lambda w : get_ret_vol_sr(w)[0] - possible_return})

    result = minimize(min_vol, initial_guess, constraints=cons , bounds=bounds, method='SLSQP')
    #print('result', result)
    frontier_vol.append(result['fun'])

#print('frontier_vol ',frontier_vol)
plt.figure(figsize=(12,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')



# Add frontier line
plt.plot(frontier_vol,frontier_y,'g--',linewidth=3)
plt.show()