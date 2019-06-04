#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:26:47 2019

@author: sercangul
"""
import math
import os
import random
import re
import sys

def central_limit_theorem(x, n, mu, sigma):
    z = (x - mu*n)/(sigma*math.sqrt(n)*math.sqrt(2))
    erf = math.erf(z)
    cum_prob = (1/2)*(1 + erf)
    return cum_prob

if __name__ == '__main__':
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    #arr = list(map(int, input().rstrip().split()))
    answer = round(central_limit_theorem(n1, n2, n3, n4), 4)
    print(answer)