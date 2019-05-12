#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10 Days of Statistics
Day 0: Mean, Median, and Mode
Created on Sun May 12 11:41:50 2019

@author: SercanGul
"""
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))