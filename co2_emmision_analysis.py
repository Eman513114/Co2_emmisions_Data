#!/usr/bin/env python
# coding: utf-8

# In[162]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[163]:


# upload data
df=pd.read_csv('co2_emission.csv')
df.head(2)


# # Asessing Data

# In[164]:


# what are the countries in this data?
df['Entity'].unique()


# In[165]:


# number of counties shared in this data
df['Entity'].nunique()


# In[166]:


# number of countries which have code[abbreviation]
# which mean there are 11 country without a code
df['Code'].nunique()


# In[167]:


list_col=list(df.columns)
for col in list_col:
    value=df[col].isnull().sum()
    print(col+ ':'+str(value))


# In[168]:


df['Code'].nunique()


# In[169]:


df['Entity'].nunique()


# In[170]:


df.groupby('Entity')['Annual CO₂ emissions (tonnes )'].sum().sort_values(ascending=False).head(10)


# In[171]:


# which countries donnot have a code in this data
df[df.Code.isnull()].Entity.value_counts()


# In[172]:


df.duplicated().any()


# In[173]:


df.shape


# In[174]:


df.dtypes


# # DATA ANALYSIS 

# ## QUESTION POINTS:
# * What are the most 20 countries produce the largest amount of pollution?
# * Express the relation between the amount of pollution across the years in line chart for top 3 countries ?
# * show the distribution of pollution amount for the top 3 countries which reduced their pollution amount?
# * Express the relation between the years and the total amount of pollution in it in a chart ?
# * What is the average for increasing in pollution amount across the years?

# # FIRST point :
# ### What are the most 20 countries produce the largest amount of pollution ?

# In[175]:


df_top20=df.groupby('Entity')['Annual CO₂ emissions (tonnes )'].sum().sort_values(ascending=False).head(20)
df_top20=pd.DataFrame(df_top20.reset_index())
df_top20


# ## The distribution of pollution amount through years for top 3 countries in pollution( united states , EU-28 , china)
# 

# * **UNITED STATES**

# In[176]:


#United States
df[df['Entity']=='United States'].plot(x ='Year', y='Annual CO₂ emissions (tonnes )',kind = 'scatter')
plt.show()


# In[177]:


# in last 30 year
df[df['Entity']=='United States'].plot(x ='Year', y='Annual CO₂ emissions (tonnes )',kind = 'scatter')
plt.xlim(1980, 2017)
plt.show()


# * **EU-28**

# In[178]:


#EU-28
df[df['Entity']=='EU-28'].plot(x ='Year', y='Annual CO₂ emissions (tonnes )',kind = 'scatter')
plt.show()


# In[179]:


# in last 30 year
df[df['Entity']=='EU-28'].plot(x ='Year', y='Annual CO₂ emissions (tonnes )',kind = 'scatter')
plt.xlim(1980,2017)
plt.show()


# * **CHINA**

# In[180]:


#china 
df[df['Entity']=='China'].plot(x ='Year', y='Annual CO₂ emissions (tonnes )',kind = 'scatter')
plt.show()


# In[181]:


# in last 30 year
df[df['Entity']=='China'].plot(x ='Year', y='Annual CO₂ emissions (tonnes )',kind = 'scatter')
plt.xlim(1980,2017)
plt.show()


# #  show the distribution of the summation pollution amount for the last years for each country?
# 

# In[182]:


d=df['Year'].sort_values(ascending=True).unique()[-3:]
data_last3years=df[df.Year.isin(d)]
data_last3years=data_last3years.groupby('Entity')['Annual CO₂ emissions (tonnes )'].sum()
data_last3years=pd.DataFrame(data_last3years.reset_index())
data_last3years.sort_values('Annual CO₂ emissions (tonnes )',ascending=False)


# ### Comment:
# * from the data we see china ,united states ,Asia and Pacific are the top countries which produce the huge amounts from co2 ,which tell us there are an increase in industry and cars.
#  

# # For all countries the distribution of co2 amounts across the years .

# In[183]:


entities=list(df['Entity'].unique())
for entity in entities:
    print(df[df['Entity']==entity].plot(x ='Year', y='Annual CO₂ emissions (tonnes )',kind = 'scatter',title=entity))


# # the relation between the years and the pollution amounts in last 50 years

# In[184]:


df_years=df.groupby('Year')['Annual CO₂ emissions (tonnes )'].sum()
df_years=pd.DataFrame(df_years.reset_index()).sort_values('Year',ascending=False).head(70)
df_years


# In[185]:


df_years.plot(x ='Year', y='Annual CO₂ emissions (tonnes )',kind = 'scatter',title='years$total amount')


# # What is the average for increasing in pollution amount across the years?

# In[186]:


df_years['Average']=df_years['Annual CO₂ emissions (tonnes )']/df_years.shape[0]
df_years.sort_values('Average',ascending=False).head(20)


# # comment:
# * as shown in the results there is increase in the Average from year and year except (2008-2009 )[as the average amount in 2009 is less than 2008 with avery small diference ,reached to .02 only in average]
