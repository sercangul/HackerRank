#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:02:33 2019

@author: sercangul
"""

def maxConsecutiveOnes(x): 
  
    # Initialize result 
    count = 0
   
    # Count the number of iterations to 
    # reach x = 0. 
    while (x!=0): 
      
        # This operation reduces length 
        # of every sequence of 1s by one. 
        x = (x & (x << 1)) 
   
        count=count+1
      
    return count

if __name__ == '__main__':
    n = int(input())
    result = maxConsecutiveOnes(n)
    print(result)