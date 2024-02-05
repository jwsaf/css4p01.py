# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:37:07 2024

@author: u92166262
"""

### Project 1 Coding Summer School 2024

import pandas as pd


file = pd.read_csv("movie_dataset.csv")

### can see Revenue and Metascore have missing values
## revenue has 1000-872 = 128 missing values
### metascore has 1000-936 = 64 missing values
print(file.info())
print(file.describe())

# view the first few rows
print(file.head(20))



#rename 2 column names that have spaces in names
file = file.rename(columns={'Revenue (Millions)': 'RevenueMillions', 'Runtime (Minutes)': 'RuntimeMinutes'})


# missing values, replace by median, as just assume the 2 variables 
## will not have Gaussian distributions, like most continues type
## data in the real world

z = file["RevenueMillions"].mean()

file["RevenueMillions"].fillna(z, inplace = True)

zz = file["Metascore"].mean()

file["Metascore"].fillna(zz, inplace = True)


## check if replaced missing values
print(file.info())


# quiz question 1

print(file["Rating"].describe())

print(file[file["Rating"] == 9])


# quiz question 2

print(file["RevenueMillions"].mean())


# quiz question 3

# the latest date is 2016, there is no 2017
print(file["Year"].describe())
xx = (file[file["Year"] >= 2015])

print(xx.info())
print(xx.describe())


print(xx["RevenueMillions"].mean())

# quiz question 4

print(file["Year"].describe())
yy = (file[file["Year"] == 2016])

print(yy.info())
print(yy.describe())



# quiz question 5

zz = (file[file["Director"] == "Christopher Nolan"])

print(zz.info())
print(zz.describe())

# quiz question 6

tt = (file[file["Rating"] >= 8])

print(tt.info())
print(tt.describe())


# quiz question 7

zz = (file[file["Director"] == "Christopher Nolan"])

print(zz.info())
print(zz.describe())

print(zz["Rating"].median())


# quiz question 8

byyear = file.groupby('Year')
     
xx = (byyear["Rating"].mean())               
print(xx)  


     
### I  checked using a longer version and really 2007

y2007 = (file[file["Year"] == 2007])
print(y2007["Rating"].describe())




# quiz question 9


### No idea so no answer, I know how to get this in SAS, but not Python

## I just took a guess to answer the question


# quiz question 10

file.apply(pd.value_counts).T.fillna(0)
file.apply(pd.value_counts).T.stack().plot kind='bar')

### got stuck no time to sort this one, I know how to do this in SAS

## I just took a guess to answer the question




# quiz question 11

### got stuck no time to sort this one, I know how to do this in SAS

## I just took a guess to answer the question



# quiz question 12

import matplotlib.pyplot as plt
import seaborn as sn

corr_matrix = file.corr()

print(corr_matrix)

sn.heatmap(corr_matrix, annot=True)
plt.show()

   
    
    

# quiz question 13

# see in the quiz the weblink



