import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2


# FUNCTIONAL

# plt.subplot(1,2,1)
# plt.plot(z,y,'r')
# plt.subplot(1,2,2)
# plt.plot(y,z,'b')
#
#
# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(z,y)
# axes.set_xlabel('X')
# axes.set_ylabel('Y')
# axes.set_title('Plots')

# OBJECT-ORIENTED

# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
# axes1.plot(z,y)
# axes2.plot(y,z)

# fig,axes = plt.subplots(nrows=1,ncols=2)
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.tight_layout()

# fig = plt.figure(figsize= (3,2))
# axes1 = fig.add_axes([0,0,1,1])
# axes1.plot(x,y)

# fig,axes = plt.subplots(nrows=2,ncols=1 , figsize=(8,2))
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.tight_layout()
#
# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes1.plot(x,x**2,label='X^2')
# axes1.plot(x,x**3, label= 'X^3', color = 'red', lw = 3, alpha = 1, ls = '-', marker = 'o', markersize = 5,
#            markerfacecolor = 'blue', markeredgewidth = 3 , markeredgecolor = 'green')
#
# axes1.legend()

#
# fig, ax = plt.subplots(figsize=(12,6))
#
# ax.plot(x, x+1, color="red", linewidth=0.25)
# ax.plot(x, x+2, color="red", linewidth=0.50)
# ax.plot(x, x+3, color="red", linewidth=1.00)
# ax.plot(x, x+4, color="red", linewidth=2.00)
#
# # possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
# ax.plot(x, x+5, color="green", lw=3, linestyle='-')
# ax.plot(x, x+6, color="green", lw=3, ls='-.')
# ax.plot(x, x+7, color="green", lw=3, ls=':')
#
# # custom dash
# line, = ax.plot(x, x+8, color="black", lw=1.50)
# line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...
#
# # possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
# ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
# ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
# ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
# ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')
#
# # marker size and color
# ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
# ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
# ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
# ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
#         markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");
#
#
#
# plt.show()


#EXCERCISE

x = np.arange(0,100)
y = x*2
z = x**2


# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# axes.set_xlabel('X')
# axes.set_ylabel('Y')
# axes.set_title('title')
#
# axes2 = fig.add_axes([0.2,0.5,.2,.2])
# axes2.plot(x,z)
#
# axes2.set_xlim(1,22)
# axes2.set_ylim(20,50)
# axes2.set_xlabel('X')
# axes2.set_ylabel('Z')
# axes2.set_title('title')
#
# fig,axes = plt.subplots(nrows=1, ncols=2)
# axes[0].plot(x,y,ls='--',color = 'r', marker='o' )
# axes[1].plot(x,z, ls='-.', marker = '+')
# plt.show()


fig,axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))
axes[0].plot(x,y,ls='--',color = 'r', marker='o' )
axes[1].plot(x,z, ls='-.', marker = '+')
plt.show()

