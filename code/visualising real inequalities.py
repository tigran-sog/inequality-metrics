# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:25:36 2024

@author: user
"""

######### CODING ATKINSON INDEX IN PYTHON ##########

import numpy as np
import pandas as pd
import seaborn as sns


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
countries = ['Nigeria','Brazil','United States','Sweden','Armenia','Czech Republic']

df_subset = df[df['country'].isin(countries)]


## Plotting
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels
def yaxis_format(y, pos):
    return f'{int(y):,}'

# Use the 'fivethirtyeight' style for the plot
plt.style.use("fivethirtyeight")

# Set the size of the figure
plt.figure(figsize=(40, 32))


# Create the line plot
line = sns.lineplot(
    x='group', y='RRinc', 
    hue='country', 
    data=df_subset,
    linewidth=15,
    legend='full'
)

# Set the y-axis to a logarithmic scale
plt.yscale('log')

# Use FuncFormatter to format the y-axis labels
plt.gca().yaxis.set_major_formatter(FuncFormatter(yaxis_format))

# Adjust font size of plot elements
plt.tick_params(axis='both', which='major', labelsize=60)  # Adjust font size for x and y axes
plt.legend(title='Country', title_fontsize=60, fontsize=40, markerscale=5,
           frameon=True, facecolor='#FCFCFC')
plt.xlabel('Income decile', fontsize=60, labelpad=30)
plt.ylabel('Real annual income ($)', fontsize=60, labelpad=30)
plt.ylim(80,100000)
plt.title('Income per decile for selected countries', fontsize=90, pad=50, loc='left',  color = '#1D5B79')
#plt.tight_layout()

plt.savefig('viz/real income distributions.png')  # Save the figure
# Show the plot
plt.show()

