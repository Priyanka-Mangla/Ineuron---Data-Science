#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install mysql-connector-python')


# In[3]:


import mysql.connector as conn


# In[4]:


mydb = conn.connect(host="localhost", user="root", password="priyanka")


# In[5]:


cursor = mydb.cursor()


# In[6]:


cursor.execute("show databases")


# In[7]:


cursor.fetchall()


# In[8]:


cursor = mydb.cursor()


# create a database called as carbon_nanotubes
# 
# E:\ineuron\datasets

# In[9]:


cursor.execute("create database carbon_nanotubes")


# In[10]:


cursor.execute("show databases")


# In[11]:


cursor.fetchall()


# create a table called as carbon with a column name given in dataset description
# 
# Data columns name:-
# 
# Chiral indice n;
# Chiral indice m;
# Initial atomic coordinate u;
# Initial atomic coordinate v;
# Initial atomic coordinate w;
# Calculated atomic coordinates u';
# Calculated atomic coordinates v';
# Calculated atomic coordinates w'

# In[18]:


cursor.execute('create table carbon_nanotubes.carbon(Chiral_indice_n VARCHAR(30), Chiral_indice_m VARCHAR(30), Initial_atomic_coordinate_u VARCHAR(30), Initial_atomic_coordinate_v VARCHAR(30), Initial_atomic_coordinate_w VARCHAR(30), Calculated_atomic_coordinates_u VARCHAR(30), Calculated_atomic_coordinates_v VARCHAR(30), Calculated_atomic_coordinates_w VARCHAR(30))')


# In[19]:


cursor.execute("use carbon_nanotubes")


# In[20]:


cursor.execute("show tables")


# In[21]:


cursor.fetchall()


# read carbon_nanotubes excel file
# 
# Data columns name:-
# 
# Chiral indice n;
# Chiral indice m;
# Initial atomic coordinate u;
# Initial atomic coordinate v;
# Initial atomic coordinate w;
# Calculated atomic coordinates u';
# Calculated atomic coordinates v';
# Calculated atomic coordinates w'

# In[27]:


import csv
with open('carbon_nanotubes.csv','r')as f:
    carbon_data = csv.reader(f, delimiter = '\n')
    for i in carbon_data:
        row_data = i[0].split(';')
        print(row_data)
        query = "insert into carbon_nanotubes.carbon values('{}','{}','{}','{}','{}','{}','{}','{}')".format(str(row_data[0]),str(row_data[1]),str(row_data[2]),str(row_data[3]),str(row_data[4]),str(row_data[5]),str(row_data[6]),str(row_data[7]))
        cursor.execute(query)        
mydb.commit()                                                                                                       


# In[29]:


cursor.execute('select * from carbon_nanotubes.carbon')


# In[30]:


cursor.fetchall()


# In[31]:


query = 'select Chiral_indice_n, count(*) from carbon_nanotubes.carbon group by Chiral_indice_n'
cursor.execute(query)
cursor.fetchall()


# In[ ]:




