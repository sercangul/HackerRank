#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:02:33 2019

@author: sercangul
"""
if __name__ == '__main__':
    n = int(input())
    final = []
    for _ in range(n):
        name = str(input())
        print(name[::2], name[1::2])