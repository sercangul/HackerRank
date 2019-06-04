#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:19:34 2019

@author: sercangul
"""

import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))