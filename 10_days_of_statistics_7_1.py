#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:19:34 2019

@author: sercangul
"""
def mean(arr,n):
    return sum(arr)/n

def stdev(arr,n):
    mean = sum(arr)/n
    return (sum([(i - mean)**2 for i in arr]) / n)**0.5

def cov(arr1,arr2):
    mean1 = sum(arr1)/n
    mean2 = sum(arr2)/n
    return sum([(arr1[i] - mean1) * (arr2[i] -mean2) for i in range(n)])

if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(float, input().rstrip().split()))
    arr2 = list(map(float, input().rstrip().split()))
    correlation_coefficient = cov(arr1,arr2)/(n*stdev(arr1,n)*stdev(arr2,n))
    print(round(correlation_coefficient,3))