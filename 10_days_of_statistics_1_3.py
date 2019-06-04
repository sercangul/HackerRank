#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:19:34 2019

@author: sercangul
"""

N = map(int,input().split())
A = list(map(int, input().strip().split(' ')))

mean = sum(A)/len(A)
i=0
X=0
while i<len(A):
    X = X + ((A[i] - mean)**2)
    i = i+1
STD = (X/len(A)) ** (0.5)

print(round((STD),1))