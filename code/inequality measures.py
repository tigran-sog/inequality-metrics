# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:00:52 2024

@author: user
"""

import numpy as np
import pandas as pd
import seaborn as sns
import math
import matplotlib.pyplot as plt
from scipy.stats import gmean
from scipy.stats import spearmanr


#### Generating income distributions


#### Downloading existing income distributions
#/ From Milanovic et al 2013, annual income per decile 1998-2008

df = pd.read_stata('data/milanovic.dta')


## Filter for only the largest 'year' values for each 'country'
# This gets me a bunch of years around 2008
df = df[df['year'] == df.groupby('country')['year'].transform('max')]

# Remove any countries with at least one NAN in their income distributions
df = df.groupby('country').filter(lambda x: x['RRinc'].notna().all())


######### CODING ATKINSON INDEX IN PYTHON ##########
income_dist = df[df['country'] == 'Armenia'].iloc[:,10]


def atkinson_index(income_dist, aversion_parameter):    
    try:
        E = float(aversion_parameter)
    except ValueError:
        print("The input is not a valid number.")
    
    if E == 1:
        geometric_mean = gmean(income_dist)
        arithmetic_mean = np.mean(income_dist)
        atkinson = 1 - geometric_mean / arithmetic_mean
        return atkinson
    
    
    elif E < 0:
        print('Please specify a value above 0.')
        return atkinson_index(income_dist) # Restarts the function
    
    else: #if E is 0 <= and not 1
        atkinson_exponent = 1 - E
        
        generalised_mean = math.pow(np.sum(np.power(income_dist, atkinson_exponent)) / len(income_dist), 1 / atkinson_exponent)
        arithmetic_mean = np.mean(income_dist)
        atkinson = 1 - generalised_mean / arithmetic_mean
        
        return atkinson
    
atkinson = atkinson_index(income_dist,1)
print(atkinson)


######### CODING GINI COEFFICIENT IN PYTHON ##########

def gini_coefficient(income_dist):
    # Create an array of order rankings (1-based index)
    order_ranking = np.arange(1, len(income_dist) + 1)
    
    # Multiply each element by its order ranking
    result = income_dist * order_ranking
    
    # Calculate Gini coefficent
    gini = (2*np.sum(result)) / (len(income_dist)*np.sum(income_dist)) - ((len(income_dist) + 1) / len(income_dist))
    
    return gini

gini = gini_coefficient(income_dist)
print(gini)


######### COMPARING INEQUALITY METRICS ###########
###### Atkinson vs. Gini #####
#### Correlation between Atkinson and Gini values for all countries, varying Atkinson by aversion parameter

atkinson_results = []
atkinson_parameter_range = np.arange(0,10.01,.01)

for country in df['country'].unique():
    income_distribution = df[df['country'] == country]['RRinc'].values
    # Calculate Atkinson indices
    for parameter in atkinson_parameter_range:  # Vary parameter from 0 to 2 by 0.01 steps
        inequality = atkinson_index(income_distribution, parameter)
        atkinson_results.append({'country': country, 'metric': 'Atkinson', 'inequality': inequality, 'parameter': parameter})
        
gini_results = []
for country in df['country'].unique():       
    income_distribution = df[df['country'] == country]['RRinc'].values
    # Calculate Gini coefficient
    gini = gini_coefficient(income_distribution)
    gini_results.append({'country': country, 'metric': 'Gini', 'inequality': gini})



# Convert results to DataFrame and display
atkinson_results_df = pd.DataFrame(atkinson_results)
gini_results_df = pd.DataFrame(gini_results)

corr_results = []

for parameter in atkinson_parameter_range:
    corr = spearmanr(atkinson_results_df[atkinson_results_df['parameter'] == parameter].iloc[:,2],
              gini_results_df.iloc[:,2])[0]
    corr_results.append({'coefficient':corr})
corr_results_df = pd.DataFrame(corr_results)

# Plot correlation
plt.figure(figsize=(15, 5))
plt.plot(atkinson_parameter_range[1:], corr_results_df['coefficient'][1:], label='Spearman coefficient') #excluding parameter = 0
plt.title('Correlation between Atkinson and Gini')
plt.xlabel('Aversion parameter')
plt.ylabel('Correlation between Atkinson and Gini')
plt.grid(True)
plt.legend()
plt.show()


### Compare relationships between IHDI and Gini coefficents for all countrys per parameter
example_parameters = [0.25, 0.5, 0.75, 1, 1.5, 2, 4]

plt.figure(figsize=(15, 15))
for parameter in example_parameters:
    atkinsons = atkinson_results_df[atkinson_results_df['parameter'] == parameter].iloc[:,2]
    plt.scatter(gini_results_df.iloc[:,2],atkinsons,label=f'parameter = {parameter}')
plt.plot((0,1), (0,1), linestyle='--', color='gray', linewidth=1, label='x = y')
plt.title('Correlation between Atkinson and Gini')
plt.xlim(0,1)
plt.ylim(0,1)
plt.ylabel('Atkinson index')
plt.xlabel('Gini index')
plt.grid(True)
plt.legend()
plt.show()


'''
### Compare relationships between IHDI and Gini coefficents for all countrys per parameter (coloured by region)
regions = df.drop_duplicates(subset='country')['region']
colors = plt.cm.tab20(np.linspace(0, 1, len(regions)))
color_map = dict(zip(regions, colors))

plt.figure(figsize=(30, 15))
for index, parameter in enumerate(example_parameters):
    plt.subplot(2, 3, index+1)
    atkinsons = atkinson_results_df[atkinson_results_df['parameter'] == parameter].iloc[:,2]
    plt.scatter(gini_results_df.iloc[:,2],atkinsons,
                label=f'parameter = {parameter}',
                color = color_map[region])
    plt.title(f'parameter = {parameter}')
    plt.ylabel('Atkinson index')
    plt.xlabel('Gini index')
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()
'''

##### TESTING IHDI LOSS OF SAME SLOPE SHIFTING UPWARDS

x = [100,1000,5000,10000,100000]
y = [2,5,10]

for i in x:
    for j in y:
        dist = np.linspace(i,i*j,10)
        loss = atkinson_index(dist,1)
        print('x:',i,'y:',j,'loss:',loss)
        
        
        
##### Parameter vs. Atkinson loss for individual countries
countries = ['Nigeria','Brazil','Armenia','United States','Sweden','Czech Republic']

plt.figure(figsize=(15, 15))
for i, c in enumerate(countries):
    plt.subplot(2,3,i+1)
    plt.plot(atkinson_results_df[atkinson_results_df['country'] == c].iloc[:,3],
             atkinson_results_df[atkinson_results_df['country'] == c].iloc[:,2])
    plt.title(f'{c}')
    #plt.xlim(0,1)
    plt.ylim(0,1)
    plt.ylabel('Atkinson index')
    plt.xlabel('Inequality aversion parameter')
    plt.grid(True)

plt.legend()
plt.show()


