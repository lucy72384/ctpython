# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:54:12 2021

@author: user
"""

guesstimes=0#設定猜測數字起始是0次
name=str(input("嗨請輸入你的貴姓大名:"))

import random
ans=random.randint(1,101)


print("嗨",name,"請輸入1-100整數猜數:")

guess=int(input())
while guesstimes in range(5):
    print("繼續猜")

    if guess>ans:
        print("猜小一點")
        print("嗨",name,"請輸入1-",guess,"的整數")
        guess=int(input())
        guesstimes+=1

    if guess<ans:
        print("猜大一點")
        print("嗨",name,"請輸入",guess,"-",guess,"的整數")
        guess=int(input())
        guesstimes+=1
        break
    if guess==ans:
        break
    

if guess==ans:
    guesstimes=int(guesstimes+1)
    print("太厲害了!",name,"猜第",guseetimes,"次就猜對了!")

if guess!=ans:
    ans=str(ans)
    print("抱歉,",name,"您已猜錯5次，終極密碼是:",ans)

