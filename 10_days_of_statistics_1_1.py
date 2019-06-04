#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:19:34 2019

@author: sercangul
"""

n=int(input())
data=sorted(list(map(int,input().split())))
Median = (data[n // 2] + data[-(n//2 + 1)]) // 2
Q1=(data[0:n//2][n // 4] + data[0:n//2][-(n//4 + 1)]) // 2
if(n%2==0):
    Q3=(data[n//2:][n // 4] + data[n//2:][-(n//4 + 1)]) // 2
else:
    Q3=(data[n//2+1:][n // 4] + data[n//2+1:][-(n//4 + 1)]) // 2
print(Q1)
print(Median)
print(Q3)