#!/usr/bin/env python
# coding: utf-8

# Numerical libraries
import numpy as np   


# to handle data in form of rows and columns 
import pandas as pd    


#importing seaborn for statistical plots
import seaborn as sns


#  Two different Dataframes

# In[12]:

left = pd.read_csv("RegisterData1.csv")
right  = pd.read_csv("RegisterData.csv")



print(left,'\n')


print(right, '\n','\n')


# ## Merging the DataFrames


merged=pd.merge(left,right,on='id')
print(merged)
