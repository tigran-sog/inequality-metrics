# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:33:05 2024

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

####### UTILITY FUNCTION OF INCOME

# Function based on Layard et al 2007 
def utility(income, elasticity):
    if elasticity == 1:
        return np.log(income)
    
    else:
        return ((income**(1-elasticity))-1) / (1-elasticity)

def marginal_utility(income, elasticity):
    if elasticity == 1:
        return 1 / income
    else:
        return income**(-elasticity)

        
# Generate data points for income
I = np.arange(1, 100000)  # Start from 1 to avoid log(0)


#### multiple elasticities
# List of different elasticity values
elasticities = [0, 0.8, 0.9, 1, 1.1, 1.2]
elasticities = [0.75, 1, 1.25]


plt.figure(figsize=(15, 5))

# Plot utility functions for different elasticities
plt.subplot(1, 2, 1)
for elasticity in elasticities:
    utils = utility(I, elasticity)
    plt.plot(I, utils, label=f'$\\rho = {elasticity}$')
plt.title('Utility Function of Income for Different Elasticities', color = '#1D5B79')
plt.xlabel('Income')
plt.ylabel('Utility')
plt.yscale('log')
plt.grid(True)
plt.legend(loc = 'upper right')

# Plot marginal utilities for different elasticities
plt.subplot(1, 2, 2)
for elasticity in elasticities:
    MU = marginal_utility(I, elasticity)
    plt.plot(I, MU, label=f'$\\rho = {elasticity}$')
    

plt.title('Marginal Utility of Income for Different Elasticities', color = '#1D5B79')
plt.xlabel('Income')
plt.ylabel('Marginal Utility')
plt.yscale('log')
plt.grid(True)
plt.legend(loc = 'upper right')

plt.tight_layout()
plt.savefig('viz/utility across elasticity.png')
plt.show()