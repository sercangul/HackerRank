#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10 Days of Statistics
Day 0: Weighted Mean
Created on Sun May 12 11:41:50 2019

@author: SercanGul
"""

N = map(int,input().split())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
sum_X = sum([a*b for a,b in zip(X,W)])
print(round((sum_X/sum(W)),1))