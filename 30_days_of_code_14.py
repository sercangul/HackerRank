#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:04:22 2019

@author: sercangul
"""

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        t = self.__elements
        k = []
        j = 1
        while j<len(t):
            i = 0
            while i<len(t)-j:
                k.append(abs(t[i] - t[i+j]))
                i = i+1
            j = j+1
        
        self.maximumDifference = max(k)

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)