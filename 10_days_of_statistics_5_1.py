#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:19:34 2019

@author: sercangul
"""

import math
x= float(input())
y= float(input())
P = (x**y)*(2.71828**(-x))/(math.factorial(y))
print (round(P,3))