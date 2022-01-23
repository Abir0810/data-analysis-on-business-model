#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd


# In[21]:


df=pd.read_csv(r"C:\Users\Abir.DESKTOP-U8C2SSO\Downloads\DA Intern_Sales&MKT - Sheet1.csv")


# In[22]:


df.head(2)


# In[35]:


from matplotlib import pyplot as plt 


# In[36]:


b=('7-24-2016','1-17-2016','6-11-2017')


# In[37]:


a=(0.5,0.43,0.41)


# In[41]:


plt.scatter(a,b)
plt.ylabel("Dates")
plt.xlabel("ROI")
plt.title("Highest 3 roi")
plt.show()


# In[45]:


plt.bar(df.customer_age,df.state,color='green',)
plt.xlabel('Age')
plt.ylabel('')
plt.title('graphic representation of relation of age & state')


# In[51]:


plt.bar(df.customer_gender,df.year,color='black',)
plt.xlabel('Gender')
plt.ylabel('')
plt.title('Gender For 2016')


# In[58]:


plt.scatter(df.customer_gender,df.year,color='red',)
plt.xlabel('Gender')
plt.ylabel('')
plt.title('Gender in 2015 and 2016')


# In[ ]:




