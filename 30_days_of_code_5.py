#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
30 Days of Code
Day 0: Hello World
Created on Mon Jun  3 18:46:54 2019
@author: SercanGul
"""

if __name__ == '__main__':
    n = int(input())
    i = 1
    while i<11:
        print("{} x {} = {}".format(n, i, (n*i)))
        i=i+1