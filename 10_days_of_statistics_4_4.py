#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:26:47 2019

@author: sercangul
"""

a, b = map(float, input().split())
x= float(input())
print(round(sum([(1 - (a / b))**(5 - x) * (a / b) for x in range(1, 6)]), 3))