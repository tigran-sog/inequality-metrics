# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:11:23 2024

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.stats import gmean

E_array = ['Gini',0.5,1,1.5]

def atkinson(dist, x, position, E):
    dist[position] = x
    dist = np.array(dist, dtype=float)  # Ensure dist elements are floats

    p = 1 - E
    if p == 0:
        return 1 - (gmean(dist) / np.mean(dist))
    else:    
        return 1 - (((np.sum(np.power(dist,p)) / len(dist))**(1/p)) / np.mean(dist))



def gini(income_dist, x, position):
    income_dist[position] = x
    income_dist = np.array(income_dist, dtype=float)  # Ensure dist elements are floats

    # Create an array of order rankings (1-based index)
    order_ranking = np.arange(1, len(income_dist) + 1)
    
    # Multiply each element by its order ranking
    result = income_dist * order_ranking
    
    # Calculate Gini coefficent
    gini = (2*np.sum(result)) / (len(income_dist)*np.sum(income_dist)) - ((len(income_dist) + 1) / len(income_dist))
    
    return gini


def plot_inequality(dist, position, x_range, E_array):
   #x_array = np.arange(dist[position-1]+0.01,dist[position-1]+x_range,0.01)
   x_array = np.arange(dist[position]-(x_range/2),dist[position]+(x_range/2),0.01)
   
   
   dist_title = dist.copy()
   dist_title[position] = 'x'
   for E in E_array:
        if E == 'Gini':
            plt.plot(x_array, np.array([gini(dist, x, position) for x in x_array]),
                     label = 'Gini')
        else:
            plt.plot(x_array, np.array([atkinson(dist, x, position, E) for x in x_array]),
                     label = f'E = {E}')
   plt.yticks(np.arange(0,1.1,0.1))
   plt.title(f'Varying E for generalised means {dist_title}')
   plt.ylabel('Generalisd mean')
   plt.xlabel('x')
   plt.tight_layout()
   plt.grid(True)
   plt.legend(loc = 'lower right')


plt.figure(figsize=(20,20))
for i in range(0,4):
    plt.subplot(2,2,i+1)
    plot_inequality(dist = [2,4,6,8], position = i, x_range = 4, E_array = E_array)
plt.savefig('viz/gini vs atkinson quartiles dist.png')
plt.show()

