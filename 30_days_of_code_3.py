#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
30 Days of Code
Day 0: Hello World
Created on Mon Jun  3 18:46:54 2019
@author: SercanGul
"""
if __name__ == '__main__':
    N = int(input())

    if N%2 != 0:
        print ("Weird")
    if N%2 == 0:
        if N>=2 and N<=5:
            print ("Not Weird")
        if N>=6 and N<=20:
            print ("Weird")
        if N>20:
            print ("Not Weird")