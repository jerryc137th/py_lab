# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:39:14 2021

@author: Poorish Charoenkul
"""

name = input("Name : ")
k = True
for i in name:
    if i == " " or i == ".":
        k = False
        break
if k:
    print("'",name,"' contains blank or period: False")
else:
    print("'",name,"' contains blank or period: True")