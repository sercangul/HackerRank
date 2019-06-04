#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:02:33 2019

@author: sercangul
"""
if __name__ == '__main__':
    n = int(input())
    name_numbers = [input().split() for _ in range(n)]
    phone_book = {k: v for k,v in name_numbers}
    while True:
        try:
            name = input()
            if name in phone_book:
                print('%s=%s' % (name, phone_book[name]))
            else:
                print('Not found')
        except:
            break