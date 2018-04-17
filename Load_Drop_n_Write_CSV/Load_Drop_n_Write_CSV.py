
# coding: utf-8

# # Loading Dropping and Write a file

# In[1]:


#Importing libraries
import pandas as pd
import numpy as np


# In[2]:


#loading into a dataframe using pandas
data = pd.read_csv('file.csv',encoding='utf-8',sep=";")


# In[4]:


#exploring the dataframe
data['Year_Month'].count()


# In[5]:


#reading top 10 rows
data.head(10)


# In[6]:


#Dropping unecessary rows
new_data=data[data.Year_Month != '2018']


# In[7]:


#Writting new file
new_data.to_csv('new_file.csv')

