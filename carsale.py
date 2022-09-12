#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.optimize import minimize
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


import pandas as pd
tbl=pd.read_excel('regcar.xlsx')
tbl


# In[8]:


import statsmodels.api as sm
x=tbl['TV Ads']
y=tbl['car Sold']
x2=sm.add_constant(x)
modl=sm.OLS(y,x2)
modl2=modl.fit()
print(modl2.summary())


# In[9]:


e=modl2.resid


# In[10]:


e


# In[11]:


np.std(e)


# In[15]:


lik_model = minimize(lik, np.array([5,5,5]),method='Nelder-Mead')


# In[19]:


def lik(parameters):
    m=parameters[0]
    b=parameters[1]
    sigma=parameters[2]
    for i in np.arrange(0,len(x)):
        y_exp=m * x + b
        L=(len(x)/2 * np.log(2 * np.pi) + len(x)/2 *np.log(sigma**2) + 1 /
        (2*sigma**2)*sum((y-y_exp)**2))
        return l


# In[20]:


lik_model = minimize(lik, np.array([5,5,5]),method='Nelder-Mead')


# In[21]:


lik_model = minimize(lik, np.array([5,5,5]),method='Nelder-Mead')


# In[22]:


lik_model = minimize(lik, np.array([5, 5, 5]), method = 'Nelder-Mead')


# In[23]:


def lik(parameters):
    m = parameters[0]
    b = parameters[1]
    sigma = parameters[2]
    for i in np.arange(0, len(x)):
        y_exp = m * x + b
        L = (len(x)/2 * np.log(2 * np.pi) + len(x)/2 * np.log(sigma ** 2) + 1 /
             (2 * sigma ** 2) * sum((y - y_exp) ** 2))
        return L


# In[24]:


lik_model = minimize(lik, np.array([5, 5, 5]), method = 'Nelder-Mead')


# In[25]:


lik_model.x


# In[26]:


plt.scatter(x,y)
plt.plot(x, lik_model['x'][0] * x + lik_model['x'][1])
plt.show()


# In[ ]:




