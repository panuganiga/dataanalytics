#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\Users\User\Downloads\employees.csv")
print(df.head())


# In[2]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\Users\User\Downloads/employees.csv")
print(df.head())


# In[3]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\Users\User\Downloads\employees.csv")
df


# In[4]:


import pandas as pd
import numpy as np


# In[5]:


df=pd.read_csv("C:/Users/User/Downloadsemployees.csv")
df


# In[6]:


df=pd.read_csv("C:/Users/User/Downloadsemployees.csv")
df


# In[7]:


df=pd.read_csv("C:/Users/User/Downloads/employees.csv")
print(df.head())


# In[8]:


print(df.dtypes)
print(df.describe())


# In[9]:


print('Salary')
print(df['Salary'].head(10))


# In[10]:


print(df['Gender'].head(10))


# In[15]:


missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df = pd.read_csv("C:/Users/User/Downloads/employees.csv",na_values=missing_value_formats)
print(df['Gender'].head(10))


# In[16]:


import pandas as pd
missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df = pd.read_csv("C:/Users/User/Downloads/employees.csv",na_values=missing_value_formats)
def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan
    df['Salary']=df['Salary'].map(make_int)
    print(df['Salary'].head())
    


# In[17]:


print(df['Salary'].head())
   


# In[18]:


print(df['Gender'].isnull().head(10))
print(df['Gender'].notnull().head(10))


# In[19]:


null_filter=df['Gender'].notnull()
print(df[null_filter].head())


# In[20]:


print(df.isnull().values.any())


# In[21]:


print(df.isnull().sum())


# In[22]:


new_df=df.dropna(axis=0)
print(new_df.isnull().values.any())


# In[23]:


new_df=df.dropna(axis=0,how='any')
new_df=df.dropna(axis=0,how='all')
new_df=df.dropna(axis=1,how='any')
new_df=df.dropna(axis=1,how='all')


# In[26]:


print("new_df")


# In[28]:


new_df=df.dropna(axis=0,how='any')
print(new_df)


# In[29]:


new_df=df.dropna(axis=0,how='all')
print(new_df)


# In[30]:


new_df=df.dropna(axis=1,how='any')
print(new_df)


# In[31]:


new_df=df.dropna(axis=1,how='all')
print(new_df)


# In[32]:


new_df=df.dropna(axis=0)
print(new_df.isnull().values.any())


# In[33]:


df['Salary'].fillna(0)


# In[34]:


df['Gender'].fillna('No Gender')


# In[35]:


df['Salary'].fillna(method='pad')


# In[36]:


df['Salary'].fillna(method='bfill')


# In[37]:


df['Salary'].interpolate(method='linear',direction='forward')


# In[ ]:




