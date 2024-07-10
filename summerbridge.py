#!/usr/bin/env python
# coding: utf-8

# In[ ]:


3 + 7 


# In[ ]:


print("hello")


# In[ ]:


name = "Aminah"
age = 42


# In[ ]:


print(age)


# In[ ]:


# This is a comment. It will not run.
#you can echo values without using print in this notebook.
name


# # Variables and values

# In[ ]:


#variables can be used in calculations
print(age)
age = age + 3
print (age)


# In[ ]:


#Order of operations matters!
first = 1 
second = first * 5
first = 2
print(first)
print(second)


# In[ ]:


#values have types. types affect what you can do with them.
print(5-3)
#print("hello"-"h")


# In[ ]:


print(len("hello"))
#print(len(6))


# ## Challenge
# Explain what each operator does
# 
# print(5//3)
# 
# print (5/3) 
# 
# print (5%3)

# In[ ]:


#Integer division
print(5//3)

#Regular division
print (5/3)

#Remainder (complement of the 1st one) 
#useful if trying to count things
print (5%3)


# # Getting help

# In[ ]:


#rounding numbers is built in
round(3.14159)


# In[ ]:


round(3.14159, 2)


# In[ ]:


help(round)


# In[ ]:


round(3.14159, ndigits=2)


# In[ ]:


#all functions return a new value
rounded_pi = round(3.14159,2)
print(rounded_pi)


# ## Challenge
# In what order do the operations happen?
# 
# radiance = 1.0
# 
# radiance = max(2.1, 2.0 +min(radiance, 1.1*radiance - 0.5))

# In[ ]:


help(min)


# In[ ]:


radiance = 1.0 
radiance = max(2.1, 2.0 +min(radiance, 1.1*radiance - 0.5))
print (radiance)


# In[ ]:


#Break down these operations
radiance = 1.0

min_arg_2 = 1.1 * radiance - 0.5
print("Min_arg_2", min_arg_2)

min_result = min(radiance, min_arg_2)
print("Min_result", min_result)

radiance = max (2.1, 2.0+ min_result)
print(radiance)


# ## A Brief Interlude with Git
# 

# In[ ]:




