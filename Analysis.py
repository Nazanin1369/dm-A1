
# coding: utf-8

# ## Data Mining Assignment 1

# ### Introduction
# In this assignment you will practice working with data and retrieving information from data. You
# will be provided with two files, edstats_country.csv and gdp_data.csv to work on this assignment.

#  ### Assignment Description

# The goal of this assignment is to get you comfortable with cleaning and analyzing data. In these
# two files you won’t need all the data to answer the questions and some of the data is missing as
# well, which you will not be using. The idea is to gather information from the available data.
# You are supposed to load the Gross Domestic Product data, gdp_data.csv, for the 190 ranked
# countries in the data set. You would also need to load the educational data provided in the file,
# edstats_country.csv to answer the following questions:
# 1. Match the data based on the country shortcode. How many of the IDs match?
# 2. Sort the data in descending order by GDP rank (so United States is last). What is the 13th
# country in the resulting data?
# 3. What is the average GDP ranking for the “High income:OECD" and “High income:nonOECD"
# group?
# 4. Cut the GDP ranking into 5 separate quantile groups. Make a table of GDP versus Income
# group. How many countries are Lower middle income but among the 38 nations with the
# highest GDP?

# ### Solution

# #### 1. Reading the data

import numpy as np
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

country_csv_path = './data/edstats_country.csv'
gdp_csv_path = './data/gdp_data.csv'

# Reading the csv file and store data in pd dataframe
countries_data = pd.read_csv(country_csv_path, index_col=0)
gdp_data = pd.read_csv(gdp_csv_path, index_col=0)

# Reading fist 10 rows
print("Total number of countries: ", countries_data.shape[0])
print("Total number of features: ", countries_data.shape[1] - 2)
#display(countries_data.head(10))

# Reading fist 10 rows
#display(gdp_data.head(20))

# Normalizing Data

# Removing columns and rows having NaNs
countries_data = countries_data.dropna(axis=1, how='all')
countries_data = countries_data.dropna(axis=0, how='all', thresh=10)

# Drop NaN indices
countries_data = countries_data[pd.notnull(countries_data.index)]
#display(countries_data.head(20))



# Removing columns and rows with NANs
gdp_data = gdp_data.dropna(axis=1, how='all', thresh=30)
gdp_data = gdp_data.dropna(axis=0, how='all', thresh=3)
# Drop NAN indices
gdp_data = gdp_data[pd.notnull(gdp_data.index)]
# Dropping unnamed columns
gdp_data = gdp_data.drop(['Economy'], axis=1)
#display(gdp_data.head(2))


# Merging both dataframes into one
data = pd.concat([gdp_data, countries_data], axis=1, join='inner')
#display(data.head(2))


# ### Answer to Question 1
print()
print('### Question one ###')
print("Total number of countries:", countries_data.shape[0])
print("Number of matched countries:", data.shape[0])
print()


# ### Answer to Question 2:
print()
print('### Question two ###')
sorted_data = data.sort(['Ranking'], ascending=[0])
print('Last country in sorted_data is United States')
display(sorted_data.tail(1)['Long Name'])
print()
# Index starts at 0, so 13th country is at index 12
thirteenth = sorted_data.iloc[[12]]
print('13th country in sorted data is: ', thirteenth['Long Name'])
#display(thirteenth)
print()

# ### Answer to Question 3:
print()
print('### Question three ###')
# Grouping data based on Income Group
income_grouped_data = data.groupby('Income Group')
grp_pass = income_grouped_data.describe()
#display(grp_pass)

# Aggregate mean for each group
means = income_grouped_data.aggregate(np.mean)
#print(means)
print('average GDP ranking for the “High income:OECD" and “High income:nonOECD" group: ')
print((income_grouped_data.get_group('High income: OECD')['Ranking'].mean() + income_grouped_data.get_group('High income: nonOECD')['Ranking'].mean() )/ 2);
print()

# ### Answer to Question 4:
print()
print('### Question four ###')
# Calculating 5 quantiles:
print('Min: ', data.Ranking.min())
print('First quantile: ', data.Ranking.quantile(0.25))
print('Median: ', data.Ranking.median())
print('Mean: ', data.Ranking.mean())
print('Second quantile: ', data.Ranking.quantile(0.75))
print('Max: ', data.Ranking.max())
print()
# Plotting 20 lowest rank GDPs
sorted_data.head(20).plot(kind='bar')
plt.savefig('./visuals/20lowestgdp.png')

# Plotting 20 highest rank GDPs
sorted_data.tail(20).plot(kind='bar')
plt.savefig('./visuals/20highesttgdp.png')


# ### GDP versus Income group
#
# As it shown below the higher the GDP ranking the Lower the income group.

# GDP Ranking vs. Income Group
sorted_data.plot(x='Income Group', y='Ranking')
plt.savefig('./visuals/gdpvsIncome.png')


# ### Countries are Lower middle income but among the 38 nations with the highest GDP
# All 38th
thirty_eight_highest_gdp = sorted_data[['Ranking', 'Income Group']].tail(38).sort_values(by=['Ranking'], ascending=[1])
thirty_eight_highest_gdp_with_low_income = thirty_eight_highest_gdp[thirty_eight_highest_gdp['Income Group'] == 'Lower middle income']
display(thirty_eight_highest_gdp_with_low_income)
print()

print('Number of High GDP countiest with low middle income  group: ', thirty_eight_highest_gdp_with_low_income.shape[0])



