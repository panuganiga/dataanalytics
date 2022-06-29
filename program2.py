#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[5]:


data=pd.read_csv('D:\pavan\gapminder_full.csv')


# In[6]:


data


# In[7]:


data.head()


# In[8]:


print(data.shape)


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[11]:


data.info()


# In[12]:


country_data=data1['country']
country_data.head()


# In[13]:


country_data=data['country']
country_data.head()


# In[14]:


country_data.tail()


# In[15]:


subset=data[['country','continent','year']]
subset.head()


# In[16]:


subset.tail()


# In[17]:


data.describe(include='all')


# In[18]:


data.hist(figsize=10,5)


# In[19]:


data.hist(figsize=(10,5))


# In[20]:


sns.boxplot(x="year",y="life_exp",data1=data)


# In[21]:


sns.boxplot(x="year",y="life_exp",data1=data)


# In[22]:


sns.boxplot(x="year",y="life_exp",data=data1)


# In[23]:


sns.boxplot(x="year",y="life_exp",data1=data)


# In[24]:


sns.boxplot(x='year',y='life_exp',data=data1)


# In[26]:


sns.boxplot(x="year",y="life_exp",data=data)


# In[27]:


data=data.drop(['year'],axis='columns')
data.head(5)


# In[28]:


data=data.rename(columns={"countr":"countries"})


# In[29]:


data=data.rename(columns={"country":"countries"})
data.head(5)


# In[30]:


duplicate_rows=data[data.duplicated()]


# In[31]:


print('number f dupli',duplicate_rows.shape)


# In[32]:


data.count()


# In[ ]:




