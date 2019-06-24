#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np  


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[20]:


data_bank = pd.read_csv('bank.csv')  # read the banl data using pandas


# In[5]:


data_bank.head(10)


# In[10]:


plt.bar(data_bank.Age,data_bank.Balance,color='red',label='age and Balance',)
plt.title('age vs Balance')
plt.xlabel("Age")
plt.ylabel('Balance')


# In[11]:


plt.scatter(data_bank.Age,data_bank.EstimatedSalary,color='red',label='Age and EstimatedSalary',)
plt.title('Age vs EstimatedSalary')
plt.xlabel("Age")
plt.ylabel('EstimatedSalary')


# In[13]:


data_bank.groupby('Geography').size().plot('pie',shadow=True, label='Geography',explode=[0.08,0,0] ,autopct='%d%%')


# In[15]:


plt.bar(data_bank.Geography,data_bank.Tenure,color='red',label='Geography and Gender',)
plt.title('Geography vs Gender')
plt.xlabel("Geography")
plt.ylabel('Gender')


# In[19]:


data_bank.groupby('Gender').size().plot('pie',shadow=True, label='Gender',explode=[0.08,0] ,autopct='%d%%')


# In[ ]:




