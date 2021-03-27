# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:38:03 2021

@author: user
"""

import random
data = []
while len(data) != 7 :
    n = random.randint(1,100)
    if ((data.count(n)==0) or (data.count(n)!=0)):
        data.append(n)
    else:
        break

data.sort()
print(data)

y=int(input("請使用者輸入串列中其一數字:")) 
while True:
    if y>data[3]:
        del data[:3]
        print(data)
        if y>data[1]:
            del data[:1]
            print(data)
            if y>data[1]:
                del data[:1]
                print(data)
                if y>data[0]:
                    del data[0]
                    print(data)
                    break
               
            elif y==data[1]:
                print(data[1])
                break
           
                
    if y<data[3]:
        del data[3:]
        print(data)
        if y<data[1]:
            del data[1:]
            print(data)
            break
        elif y==data[1]:
            print (data[1])
            break
        else: 
            y>data[1]
            del data[:1]
            print(data)
            
            if y>data[0]:
                del data[0]
                print(data)
                break
    if y==data[3]:
        print(data[3])
        break
      

print("程式執行結束")    
            



        