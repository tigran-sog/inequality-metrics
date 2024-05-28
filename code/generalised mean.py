# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:57:53 2024

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import gmean

#### PLOTTING GENERALISED MEANS

## Means of 1 and x

def generalised_mean(x, p):
    if p == 0:
        return (x**(1/2))
    else:    
        return ((1 + x**p) / 2)**(1/p)
    
def generalised_mean2(x, p):
    if p == 0:
        return gmean(x)
    else:    
        return (np.sum(np.power(x,p)) / len(x))**(1/p)

def generalised_mean_dist(x, p):
    array = [2,4,6,8]
    array[1] = x
    if p == 0:
        return geometric(x)
    else:
        np.sum(np.power(array,p)) / len()
        
        
def generalised_mean3(dist,x,position,p):
    dist[position] = x
    if p == 0: # if p 0 then set it equal to the geometric mean
        return gmean(x)
    else:
        return (np.sum(np.power(dist,p)) / len(dist))**(1/p)

E_array = [0.01,0.25,0.5,0.75,1,2,4,8,16]
x_array = np.arange(0,4.01,0.01)
dist = [1,2]

plt.figure(figsize=(10,10))
for E in E_array:
    p = 1 - E
    plt.plot(x_array, generalised_mean(x_array,p),
             label = f'E = {E}')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()


income_dists = {
   'Nigeria' : [100,500,750,1500],
   'Armenia' : [100,250,500,650],
   'Czechia' : [500, 750, 1200, 1600],
   'Sweden' : [600, 900, 1300, 1500],
   'USA' : [400, 900, 1300, 1900]
   }

for key, value in income_dists.items():
    plt.figure(figsize=(15,15))
    mean_results = []
    value = np.array(value, dtype=float)
    arithmetic_mean = np.mean(value)
    for E in E_array:
        p = 1 - E
        mean_results.append(generalised_mean2(value,p))
    plt.plot(E_array,mean_results)
    plt.xscale('log')
    plt.title(f'Generalised mean of {key}\'s income distribution\nArithmetic mean of {arithmetic_mean}')
    plt.ylabel('Generalised mean')
    plt.xlabel('Value of E')
    plt.grid()
    plt.show()
    

plt.figure(figsize=(15,15))
for key, value in income_dists.items():
    mean_results = []
    value = np.array(value, dtype=float)
    arithmetic_mean = np.mean(value)
    for E in E_array:
        p = 1 - E
        mean_results.append(generalised_mean2(value,p))
    plt.plot(E_array,mean_results, label = f'{key}')
    plt.xscale('log')
    plt.title('Generalised mean of countries\' income distributions')
    plt.ylabel('Generalised mean')
    plt.xlabel('Value of E')
    plt.legend()
plt.grid()
plt.show()