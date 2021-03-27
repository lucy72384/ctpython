# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:21:09 2021

@author: user
"""

profit=int(input("請輸入獲利金額:"))
bonus=0
while True:
    if profit<100000:
        bonus=profit*0.1
        print(bonus)
        break
    if 100000<=profit<200000:
        bonus=(100000)*0.1+(profit-100000)*0.07
        print(bonus)
        break
    if 200000<=profit<400000:
        bonus=(100000)*0.1+(100000)*0.07+(profit-200000)*0.03
        print(bonus)
        break
print("程式執行完畢")
        