#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd


# In[31]:


India_Menu_path = 'C:/Users/Shubhangam/Desktop/ML/CSV files/India_Menu.csv'


# In[32]:


India_menu_data=pd.read_csv(India_Menu_path)


# In[33]:


India_menu_data.describe()


# In[35]:


India_menu_data.columns


# In[28]:


India_menu_data = India_menu_data.dropna(axis=0)


# In[36]:


y = India_menu_data.Price


# In[37]:


India_menu_features = ['Menu_Category', 'Menu_Items', 'Per_Serve_Size', 'Energy _(kCal)', 'Protein_(g)']


# In[38]:


x=India_menu_data[India_menu_features]


# In[39]:


x.describe()


# In[40]:


x.head()


# In[ ]:




