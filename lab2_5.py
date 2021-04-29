# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:18:19 2021

@author: Poorish Charoenkul
"""

len_tri = input("Lenght of three sides:").split(",")
tri = []
for i in range(len(len_tri)):
    #tri[i] = float(len_tri[i])
    tri.append(float(len_tri[i]))
sides = sorted(tri)

if (sides[0]**2 + sides[1]**2) == sides[2]**2:
    print("Right triangle: True")
else:
    print("Right triangle: False")
