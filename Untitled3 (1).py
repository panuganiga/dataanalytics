#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


acad=pd.read_excel('C:/Users/User/Downloads/acad.xlsx')


# In[4]:


acad


# In[6]:


ods=pd.pivot_table(acad[['g','sm']],index='g',columns='sm',aggfunc=len)
ods


# In[7]:


from scipy.stats import chi2_contingency


# In[9]:


chi2,p,dof,tbl=chi2_contingency(ods)


# In[10]:


chi2


# In[11]:


p


# In[12]:


dof


# In[13]:


tbl


# In[ ]:




