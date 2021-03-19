# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:13:31 2021

@author: user
"""


a=int(input("請使用者輸入整數範圍:"))

for b in list(range(1,a+1)):
    if b%4==0:
        print(b,"是4的倍數")

#僅限找尋1-100內質數
for b in range(1,a+1):
    if b==1:
        continue  
    if b==2:
        print(b,"是質數")
    for i in range(2,b):    
        if (b==3 or b==5 or b==7):
             print(b,"是質數")
             break
        if (b%3==0 or b%5==0 or b%7==0):
             break
        if b%i!=0:
            print(b,"是質數")
            break
        if b%i==0:
            break  
            
print("程式執行完畢")


