# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:27:44 2021

@author: Poorish Charoenkul
"""

len_tri = input("Length of 3 sides:").split(",")
a,b,c = float(len_tri[0]),float(len_tri[1]),float(len_tri[2])

if a+b>c and a+c>b and b+c>a:
    print("Triangle: True")
else:
    print("Triangle: False")