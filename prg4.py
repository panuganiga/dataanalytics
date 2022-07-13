#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


obj=pd.Series(range(4),index=['d','a','b','c'])
obj.sort_index()


# In[5]:


frame=pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
frame.sort_index()


# In[7]:


frame.sort_index(axis=1)


# In[9]:


frame.sort_index(axis=1,ascending=False)


# In[10]:


obj=pd.Series([4,7,-3,2])
obj.sort_values()


# In[11]:


obj=pd.Series([4,np.nan,7,np.nan,7,np.nan,-3,2])
obj.sort_values()


# In[12]:


frame=pd.DataFrame({'a':[0,1,0,1],'b':[4,7,-3,2]})
frame


# In[13]:


frame.sort_values(by='b')


# In[14]:


frame.sort_values(by=['a','b'])


# In[15]:


obj=pd.Series([7,-5,7,4,2,0,4])
obj.rank()


# In[16]:


obj.rank(method='first')


# In[18]:


obj.rank(ascending=False,method='max')


# In[20]:


frame=pd.DataFrame({'a':[0,1,0,1],'b':[4.3,7,-3,2],'c':[-2,5,8,-2.5]})
frame


# In[21]:


frame.rank(axis='columns')


# In[ ]:




