#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
30 Days of Code
Day 2: Operators
Created on Sun May 12 11:41:50 2019
@author: SercanGul
"""
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total = round(meal_cost + (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100))
    print(total)
    return 

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)