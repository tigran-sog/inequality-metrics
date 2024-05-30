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
        atkinson_measure = 1 - (generalised_mean2(value,p) / arithmetic_mean)
        iai = arithmetic_mean * (1 - atkinson_measure)
        inequal_results.append({'country': country,
                              'income': arithmetic_mean,
                              'atkinson': atkinson_measure,
                              'inequality-adjusted income': iai,
                              'E': E})
        
inequal_results_df = pd.DataFrame(inequal_results)

        
## Plot it all

plt.figure(figsize=(15, 15))
for E in E_array:
    plt.scatter(inequal_results_df[inequal_results_df['E'] == E].iloc[:,1],
                inequal_results_df[inequal_results_df['E'] == E].iloc[:,3],
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

plt.figure(figsize=(15, 15))
for E in E_array:
    plt.scatter(inequal_results_df[inequal_results_df['E'] == E].iloc[:,2],
                inequal_results_df[inequal_results_df['E'] == E].iloc[:,3],
                label = f'E = {E}')
plt.title('Atkinson measure and inequality-adjusted income per capita across levels of E')
#plt.xlim(0,1)
#plt.ylim(0,1)
plt.ylabel('Inequality-adjusted income per capita')
plt.ylabel('Atkinson measure')
#plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.show()


##### Correlation between Atkinson E results
from scipy.stats import spearmanr

E_array = np.arange(0,2.01,.01)

other_atkinson = []

for country in df['country'].unique():
    mean_results = []
    value = df[df['country'] == country].iloc[:,10]
    
    arithmetic_mean = np.mean(value)
    for E in E_array:
        p = 1 - E
        atkinson_measure = 1 - (generalised_mean2(value,p) / arithmetic_mean)
        iai = arithmetic_mean * (1 - atkinson_measure)
        other_atkinson.append({'country': country,
                              'income': arithmetic_mean,
                              'atkinson': atkinson_measure,
                              'inequality-adjusted income': iai,
                              'E': E})
        
other_atkinson_df = pd.DataFrame(other_atkinson)
other_atkinson_df_0 = other_atkinson_df[other_atkinson_df['E'] == 0]
other_atkinson_df_rest = other_atkinson_df[other_atkinson_df['E'] != 0]


corr_results_atk = []

for parameter in E_array[1:]:
    corr = spearmanr(
              other_atkinson_df_rest[other_atkinson_df_rest['E'] == parameter].iloc[:,1],
              other_atkinson_df_rest[other_atkinson_df_rest['E'] == parameter].iloc[:,3])[0]
    corr_results_atk.append({'coefficient':corr})
corr_results_atk_df = pd.DataFrame(corr_results_atk)

# Plot correlation
plt.figure(figsize=(15, 10))
plt.plot(E_array[1:], corr_results_atk_df['coefficient'], label='Spearman coefficient') #excluding parameter = 0
plt.title('Correlation between income per capita vs. inequality-adjusted incomes per capita')
plt.xlabel('Inequality aversion parameter, E')
plt.ylabel('Spearman coefficent')
plt.grid(True)
plt.legend()
plt.show()
