#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
from scipy import stats


# In[16]:


x=stats.norm.rvs(30,10,30)
results=stats.ttest_1samp(x,27)
alpha=0.05
if(results[0]<0)&(results[1]/2<alpha):
    print("rejct null hypothesis,mean is greater than 27")
else:print("accept null hypothesis")


# In[17]:


y=stats.norm.rvs(500,10,30)
res=stats.ttest_1samp(x,505)


# In[18]:


res


# In[19]:


import math
xbar=505
SEM=(10/math.sqrt(30))


# In[20]:


mu=500
z=(xbar-mu)/SEM
z


# In[21]:


pval=2*(1-stats.norm.cdf(z))
pval


# In[23]:


alpha=0.03
if(pval<alpha):
 print("reject null hypothesis")
else:print("Accept null hypothesis")


# In[ ]:




