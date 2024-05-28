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
    dist = np.array(dist, dtype=float)  # Ensure dist elements are floats
    if p == 0: # if p 0 then set it equal to the geometric mean
        return gmean(dist)
    else:
        return (np.sum(np.power(dist,p)) / len(dist))**(1/p)

E_array = [0,0.25,0.75,1,2,4,8]

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


# Plotting generalised (2,x,6,8)
four_value_dist = [2,4,6,8] # approximating income distribution 
x_array = np.arange(2.01,6.00,0.01) # restricting x to be between first and third values
plt.figure(figsize=(10,10))
for E in E_array:
    p = 1 - E
    plt.plot(x_array, np.array([generalised_mean3(four_value_dist, x, 1, p) for x in x_array]),
             label = f'E = {E} (p = {p})')
plt.title('Varying E for generalised means of approximated income distributions')
plt.ylabel('Generalisd mean')
plt.xlabel('(2,x,6,8)')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()

# Plotting generalised (4,x,12,16) [confirms that its only relative parts of the distribution that matters]
four_value_dist = [4,8,12,16] # approximating income distribution 
x_array = np.arange(4.01,12.00,0.01) # restricting x to be between first and third values
plt.figure(figsize=(10,10))
for E in E_array:
    p = 1 - E
    plt.plot(x_array, np.array([generalised_mean3(four_value_dist, x, 1, p) for x in x_array]),
             label = f'E = {E} (p = {p})')
plt.title('Varying E for generalised means of approximated income distributions')
plt.ylabel('Generalisd mean')
plt.xlabel('(4,x,12,16)')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()


def plot_generalised_means(dist, position, x_range, E_array):
   #x_array = np.arange(dist[position-1]+0.01,dist[position-1]+x_range,0.01)
   x_array = np.arange(dist[position]-(x_range/2),dist[position]+(x_range/2),0.01)
   
   dist_title = dist.copy()
   dist_title[position] = 'x'
   plt.figure(figsize=(10,10))
   for E in E_array:
       p = 1 - E
       plt.plot(x_array, np.array([generalised_mean3(dist, x, position, p) for x in x_array]),
                label = f'E = {E} (p = {p})')
   plt.title(f'Varying E for generalised means ({dist_title})')
   plt.ylabel('Generalisd mean')
   plt.xlabel(f'{dist_title}')
   plt.tight_layout()
   plt.grid()
   plt.legend()
   plt.show()

plot_generalised_means(dist = [2,4,6,8], position = 0, x_range = 4, E_array = E_array)
plot_generalised_means(dist = [2,4,6,8], position = 1, x_range = 4, E_array = E_array)
plot_generalised_means(dist = [2,4,6,8], position = 2, x_range = 4, E_array = E_array)    
plot_generalised_means(dist = [2,4,6,8], position = 3, x_range = 4, E_array = E_array)

    
##############################################################################
##############################################################################
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