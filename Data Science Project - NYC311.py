#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[176]:


df =pd.read_csv("311_Service_Requests_from_2010_to_Present.csv")


# In[177]:


df.head()


# In[178]:


df.describe()


# In[179]:


cols=df.columns.where(df.isna().sum()>50000).dropna()
cols


# In[180]:


df['Closed Date'].isna().sum()


# In[181]:


df=df.drop(columns=cols , axis=1)
df.isna().sum()


# In[182]:


df['Park Facility Name'].value_counts()


# In[183]:


df['Park Borough'].value_counts()


# In[184]:


df['School Name'].value_counts()


# In[185]:


df['School Region'].value_counts()


# In[186]:


df['School State'].value_counts()


# In[187]:


df['School Number'].value_counts()


# In[188]:


df['School City'].value_counts()


# In[189]:


df['School Address'].value_counts()


# In[190]:


df['School Zip'].value_counts()


# In[191]:


import string as str1


# In[192]:


columns_school=[column for column in df.columns if column.startswith("School")]
columns_school


# In[193]:


df = df.drop(columns=columns_school , axis=1)


# In[194]:


df


# In[195]:


df.isna().sum()


# In[213]:


indexes_drop=df[df['Closed Date'].isna()].index
indexes_drop


# In[214]:


df = df.drop(index=indexes_drop , axis=0)
df.reset_index()


# In[218]:


df


# In[219]:


df.columns


# In[220]:


ax=sns.histplot(x=df['Complaint Type'] , hue=df['Status'])
ax.tick_params(axis='x' , rotation=90)


# In[221]:


ax=sns.scatterplot(x=df['Complaint Type'] , y=df['Agency Name'])
ax.tick_params(axis='x' , rotation=90)


# In[222]:


ax=sns.histplot(x=df['Complaint Type'] , hue=df['Agency Name'])
ax.tick_params(axis='x' , rotation=90)


# In[223]:


ax = plt.figure(figsize=(10,10))
ax=sns.countplot(x=df['Complaint Type'])
ax.tick_params(axis='x' ,labelsize=15 , rotation=90)


# In[224]:


df["Agency Name"].value_counts()


# In[225]:


df["Community Board"].value_counts()


# In[226]:


ax=plt.figure(figsize=(100,50))
ax=sns.countplot(x=df['Community Board']  )
ax.tick_params(axis='x' ,labelsize=75,  rotation=90)
ax.tick_params(axis='y' , labelsize=75)


# In[227]:


df


# In[228]:


df.columns


# In[229]:


ax=sns.countplot(x=df['Location Type'] )
ax.tick_params(axis='x' , rotation=90)


# In[230]:


from datetime import datetime


# In[231]:


df['Created Date'] = pd.to_datetime(df['Created Date'])
df['Closed Date']  = pd.to_datetime(df['Closed Date'])
df.dtypes


# In[233]:


df["Request_Closing_Time"] = df["Closed Date"] - df["Created Date"]


# In[234]:


df


# In[237]:


col = df.pop("Request_Closing_Time")
df.insert(1 , "Request_Closing_Time" , col)


# In[243]:


df = df.sort_values("Request_Closing_Time")
df=df.reset_index()


# In[244]:


df 


# In[245]:


df=df.drop("index" , axis=1)
df


# In[246]:


df.columns


# In[247]:


df['City']


# In[248]:


g = df.groupby(df["City"])


# In[250]:


df["City"].value_counts()


# In[271]:


ax = plt.figure(figsize=(20,10))
ax=sns.countplot(x=df['City'])
ax.tick_params(axis='x' ,labelsize=15 , rotation=90)
ax.tick_params(axis='y' , labelsize=15)


# In[ ]:




