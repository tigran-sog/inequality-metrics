# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:53:34 2024

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import gmean



#### Generating income distributions


#### Downloading existing income distributions
#/ From Milanovic et al 2013, annual income per decile 1998-2008

df = pd.read_stata('data/milanovic.dta')


## Filter for only the largest 'year' values for each 'country'
# This gets me a bunch of years around 2008
df = df[df['year'] == df.groupby('country')['year'].transform('max')]

# Remove any countries with at least one NAN in their income distributions
df = df.groupby('country').filter(lambda x: x['RRinc'].notna().all())

def generalised_mean2(x, p):
    if p == 0:
        return gmean(x)
    else:    
        return (np.sum(np.power(x,p)) / len(x))**(1/p)
    

inequal_results = []

E_array = [0,0.25,0.75,1,2,4]

for country in df['country'].unique():
    print(f'Running {country}')
    mean_results = []
    value = df[df['country'] == country].iloc[:,10]
    
    arithmetic_mean = np.mean(value)
    for E in E_array:
        p = 1 - E
        iai = arithmetic_mean * (generalised_mean2(value,p) / arithmetic_mean)
        inequal_results.append({'country': country,
                              'income': arithmetic_mean,
                              'inequality-adjusted income': iai,
                              'E': E})
        
inequal_results_df = pd.DataFrame(inequal_results)

        
## Plot it all

plt.figure(figsize=(15, 15))
for E in E_array:
    plt.scatter(inequal_results_df[inequal_results_df['E'] == E].iloc[:,1],
                inequal_results_df[inequal_results_df['E'] == E].iloc[:,2],
                label = f'E = {E}')
plt.title('Income and inequality-adjusted income per capita across levels of E')
#plt.xlim(0,1)
#plt.ylim(0,1)
plt.xlabel('Income per capita')
plt.ylabel('Inequality-adjusted income per capita')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.show()