#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:26:47 2019

@author: sercangul
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a, b = map(float, input().split())

p = a/(a+b)
q = b/(a+b)

x=3
n=6

def binomial(x,n,p,q):
    return (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))* (p**x) * (q**(n-x))

result = 0
while x<n+1:
    result =result + binomial(x,n,p,q)
    x = x+1

print (round(result,3))