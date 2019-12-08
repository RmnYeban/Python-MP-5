# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:10:05 2019

@author: ASUS
"""
import math as YeEt
import numpy as YEET
import matplotlib.pyplot as yEeT

yeban = YEET.arange(0,200)
x = YEET.sin(((3*YeEt.pi)/ 100) * yeban )
if yeban.all() == 0:
    y = (-1.5*x)+(2*x*(yeban+1))-(0.5*x*(yeban+2))
elif 0 < yeban and yeban <= 198:
    y = (0.5*x)*(yeban+1)-(0.5*x)*(yeban - 1)
else:
    y = 1.5*x - (2*x)*(yeban - 1) + (0.5*x)*(yeban - 2)
yEeT.plot(x,'r',label='line one',linewidth=5)
yEeT.plot(y,'g',label='line two',linewidth=5)
yEeT.grid(True,color='k')
yEeT.legend()
yEeT.xlabel('x & y with n as variable ')
yEeT.ylabel('y  w/respect to x and n ')
yEeT.show()
