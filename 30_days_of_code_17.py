#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:50:22 2019

@author: sercangul
"""

class Calculator:
    def power(self,n,p):
        if n>=0 and p>=0:
            result = n**p
        else:
            result = Exception
            result = ("n and p should be non-negative")
        return result
    
    
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   