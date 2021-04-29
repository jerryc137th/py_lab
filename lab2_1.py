# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:32:30 2021

@author: Poorish Charoenkul
"""

import math

coef = input("Enter coefficients a,b,c :").split(",")

a,b,c = float(coef[0]),float(coef[1]),float(coef[2])

rt = math.sqrt((b**2)-4*a*c)
x1 = (-b + rt)/(2*a)
x2 = (-b - rt)/(2*a)
print("x = ",x1,",",x2)










