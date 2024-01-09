#!/usr/bin/env python
# coding: utf-8

# In[5]:


fruits = ["apple","banana","cherry"]
for fruit in fruits :
    print(fruit)
    


# In[36]:


count = 0
while count < 5:
    print(count)
    count = count + 2


# In[3]:


for num in range(10):
    if num == 5:
        break
    print(num)


# In[44]:


for num in range(5):
    if num == 2:
        continue
    print(num)


# In[26]:


index = 1
for item in fruits:
    print ("fruits :", item + ","" index :", index)
    index = index + 1


# index = 1
# for item in fruits:
#     if 'apple'== item :   
#     break
#     print("the item apple is in the list at index", index)
#     index = index + 1

# In[28]:


index = 1
for item in fruits:
    if 'apple'== item :  
        break
    print("the item apple is in the list at index", index)
    index = index + 1


# In[23]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
for num in numbers:
    if num % 2 == 0:
        print(num)


# In[34]:


for i in range(1, 6):
    for j in range(1, 6):
        print(i, "x", j, "=", i * j)
    print("----------")


# In[ ]:





# In[48]:


count = 1
while count <= 10:
    print(count)
    count = count + 2
    continue

print("-----")
    
for i in range(1, 5):
    print(i)


# In[49]:


for i in range(3):
    for j in range(3):
        print(i, j)


# In[54]:


import math

for i in range(1, 6):
    for j in range(1, 6):
        print(i, "pow", j, "=", math.pow(i,j))
    print("----------")


# In[5]:


count = 1
while count <=10:
    print(count)
    count = count + 1
    continue
    
print("-------")
    
for i in range(1, 11):
    print(i)


# In[11]:


for i in range(1,11):
    if i %2 == 0:
        print(i)


# In[15]:


for i in range(1,5):
    for j in range(1,5):
        print(i, "x", j, "=", i*j)


# In[ ]:




