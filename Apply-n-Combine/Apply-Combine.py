
# coding: utf-8

# # Apply 'n Combine

# In[1]:


#Importing libraries
import pandas as pd
import numpy as np


# In[2]:


#loading into a dataframe using pandas
data = pd.read_csv('file.csv',encoding='utf-8',sep=";")


# In[3]:


#exploring the dataframe
data['Year_Month'].count()


# In[4]:


#reading top 10 rows
data.head(10)


# In[19]:


taxe = lambda x: x*0.1


# In[20]:


#apply a function along any axis of the dataframe

data_taxes = data['VL'].apply(taxe)


# In[21]:


#check some rows
data_taxes.head(10)


# In[22]:


#Append new column
data['taxe']=data_taxes


# In[23]:


#check new dataset
data.head(10)

