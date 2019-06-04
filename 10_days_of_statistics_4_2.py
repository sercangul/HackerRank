#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:26:47 2019

@author: sercangul
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
p, n = map(float, input().split())

p = p/100
q = 1-p



def binomial(x,n,p,q):
    return (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))* (p**x) * (q**(n-x))

#at least two rejects
result = 0
x=2
while x<n+1:
    result =result + binomial(x,n,p,q)
    x = x+1


atleasttwo = result
nomorethantwo = binomial(0,n,p,q)+ binomial(1,n,p,q)+ binomial(2,n,p,q)

print (round(nomorethantwo,3))
print (round(atleasttwo,3))

