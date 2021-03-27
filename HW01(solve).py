# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:31:30 2021

@author: user
"""
import random
data = []
while len(data) != 6 :
    n = random.randint(1,49)
    if data.count(n)==0:
        data.append(n)
        
print(data) 
data.sort()
data2=data
print(data2) 

        
    