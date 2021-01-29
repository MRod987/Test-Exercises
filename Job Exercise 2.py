#!/usr/bin/env python
# coding: utf-8

# In[1]:


def function(num1, num2, num3):
    values = [None]
    
    if num1 + num2 == num3:
        if values[0] == None:
            values[0] = "+"
    if num1 - num2 == num3:
        if values[0] == None:
            values[0] = "-"
        else:   
            values.append("-")
    if num1 * num2 == num3:
        if values[0] == None:
            values[0] = "*"
        else:   
            values.append("*")
    if num1 / num2 == num3:
        if values[0] == None:
            values[0] = "/"
        else:   
            values.append("/")
    return values  


# In[ ]:




