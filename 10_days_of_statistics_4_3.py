#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:26:47 2019

@author: sercangul
"""

a, b = map(float, input().split())
n = float(input())
p = a/b
q = 1-p
result = (q**(n-1))* p
print (round(result,3))