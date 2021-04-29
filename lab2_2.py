# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:17:09 2021

@author: Poorish Charoenkul
"""



coef = input("Enter coefficients a,b,c :").split(",")

a,b,c = float(coef[0]),float(coef[1]),float(coef[2])

if ((b**2)-4*a*c)>=0 and a != 0:
    print("Can use quadratic formula: True")
else:
    print("Can use quadratic formula: False")