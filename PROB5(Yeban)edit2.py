# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:10:05 2019

@author: ASUS
"""
import math as m
import numpy as n
import matplotlib.pyplot as l
yeban = n.arange(0,199)
x = n.sin(((3*m.pi)/ 100)*yeban ) #main equation to use
if yeban.all() == 0:
    y = (-1.5*x)+(2*x*(yeban+1))-(0.5*x*(yeban+2)) #if equal to 0 
elif 0 < yeban and yeban <= 198:
    y = (0.5*x)*(yeban+1)-(0.5*x)*(yeban - 1) #0<n<=198
else:
    y = 1.5*x - (2*x)*(yeban - 1) + (0.5*x)*(yeban - 2) #at 199
l.plot(x,'r',label='line one',linewidth=5)
l.plot(y,'g',label='line two',linewidth=5)
l.grid(True,color='k')
l.legend()
l.xlabel('x & y with n as variable ')
l.ylabel('y  w/respect to x and n ')
l.show()
