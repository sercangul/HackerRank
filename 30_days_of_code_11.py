#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:19:33 2019

@author: sercangul
"""

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    i= 0
    thesum = []
    while i<4:
        j=0
        while j<4:
            thesum.append(int(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]))       
            j=j+1
        i=i+1
    print (max(thesum))