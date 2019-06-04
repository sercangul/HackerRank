#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:19:34 2019

@author: sercangul
"""
from math import erf

std = 2.0
h1 = 19.5
h21,h22 = 20.0,22.0
mean = 20

def N(mean, std, x):
    return 0.5 + 0.5 * erf((x-mean)/(std* 2**0.5))

print (N(mean,std,h1))
print (N(mean,std,h22)-N(mean,std,h21))