#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:43:42 2019

@author: sercangul
"""

import sys

S = input().strip()

try:
    print(int(S))

except ValueError:
    print("Bad String")