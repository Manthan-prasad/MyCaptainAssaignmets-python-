#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:32:40 2022

@author: manthanprasad
"""

from math import pi
r = float(input("Input the radius of the circle : "))
print ("The area of the circle with radius ",r," is: ",pi*(r**2))

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + f_extns[1])