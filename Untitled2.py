#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


dataset=pd.read_csv('C:/Users/User/Downloads/retail_bakery_transactions.csv')


# In[4]:


dataset


# In[6]:


dataset.columns=dataset.columns.str.lower()


# In[7]:


dataset.head()


# In[8]:


dataset.info()


# In[10]:


dataset.isnull().sum()


# In[11]:


transactio_list=dataset.groupby(['transaction','date_time'])['item'].apply(lambda x: list(x))


# In[13]:


transactio_list.head()


# In[14]:


df=transactio_list.values.tolist()


# In[15]:


df[:5]


# In[16]:


from mlxtend.preprocessing import TransactionEncoder


# In[17]:


encoder=TransactionEncoder().fit(df)


# In[18]:


onehot=encoder.transform(df)


# In[19]:


transf_df=pd.DataFrame(onehot,columns=encoder.columns_)


# In[20]:


transf_df.head()


# In[21]:


from mlxtend.frequent_patterns import fpgrowth


# In[23]:


frequent_itemset.sort_values('support',ascending=False)


# In[ ]:





# In[ ]:




