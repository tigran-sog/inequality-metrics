# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:57:53 2024

@author: user
"""

import numpy as np
import pandas as pd
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
    dist = np.array(dist, dtype=float)  # Ensure dist elements are floats
    if p == 0: # if p 0 then set it equal to the geometric mean
        return gmean(dist)
    else:
        return (np.sum(np.power(dist,p)) / len(dist))**(1/p)

E_array = [0,0.25,0.75,1,2,4]

# Plotting generalised (1,x)
x_array = np.arange(0,4.01,0.01)
two_value_dist = [1,2]
plt.figure(figsize=(10,10))
for E in E_array:
    p = 1 - E
    plt.plot(x_array, np.array([generalised_mean3(two_value_dist, x, 1, p) for x in x_array]),
             label = f'E = {E} (p = {p})')
plt.title('Varying E for generalised means of simple mean of 1 and x')
plt.xlabel('(1,x)')
plt.ylabel('Generalisd mean')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()



def plot_generalised_means(dist, position, x_range, E_array):
   #x_array = np.arange(dist[position-1]+0.01,dist[position-1]+x_range,0.01)
   x_array = np.arange(dist[position]-(x_range/2),dist[position]+(x_range/2),0.01)
   
   # Finding maximum value for y-axis
   dist_temp = dist.copy()
   dist_temp[-1] = dist_temp[-1]+(x_range/2)
   y_max = math.ceil(np.mean(dist))+0.05 
   
   dist_title = dist.copy()
   dist_title[position] = 'x'
   for E in E_array:
       p = 1 - E
       plt.plot(x_array, np.array([generalised_mean3(dist, x, position, p) for x in x_array]),
                label = f'E = {E} (p = {p})')
   plt.yticks(np.arange(0,y_max))
   plt.title(f'Varying E for generalised means {dist_title}')
   plt.ylabel('Generalisd mean')
   plt.xlabel('x')
   plt.tight_layout()
   plt.grid(True)
   plt.legend(loc = 'lower right')

plt.figure(figsize=(10,10))
plot_generalised_means(dist = [1,3], position = 1, x_range = 4, E_array = E_array)
plt.savefig('viz/generalised mean simple dist.png')
plt.show()

plt.figure(figsize=(20,20))
for i in range(0,4):
    plt.subplot(2,2,i+1)
    plot_generalised_means(dist = [2,4,6,8], position = i, x_range = 4, E_array = E_array)
plt.savefig('viz/generalised mean quartiles dist.png')
plt.show()


    
##############################################################################
##############################################################################


#### Generating income distributions


#### Downloading existing income distributions
#/ From Milanovic et al 2013, annual income per decile 1998-2008

df = pd.read_stata('data/milanovic.dta')
## Filter for only the largest 'year' values for each 'country'
# This gets me a bunch of years around 2008
df = df[df['year'] == df.groupby('country')['year'].transform('max')]

# Remove any countries with at least one NAN in their income distributions
df = df.groupby('country').filter(lambda x: x['RRinc'].notna().all())

# Countries I want to look at
countries = ['United States','Sweden','Czech Republic','Brazil','Nigeria','Armenia']

df_subset = df[df['country'].isin(countries)]

plt.figure(figsize=(10,10))
for country in countries:
    mean_results = []
    value = df_subset[df_subset['country'] == country].iloc[:,10]
    
    arithmetic_mean = np.mean(value)
    for E in E_array:
        p = 1 - E
        mean_results.append(generalised_mean2(value,p))
    plt.plot(E_array,mean_results, label = f'{country}')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Generalised mean of countries\' income distributions')
    plt.ylabel('Generalised mean ($)')
    plt.xlabel('Inequality aversion parameter (E)')
    plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('viz/generalised means countries.png')
plt.show()
