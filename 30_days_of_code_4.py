#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
30 Days of Code
Day 0: Hello World
Created on Mon Jun  3 18:46:54 2019
@author: SercanGul
"""
class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            print ("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age<13:
            print ("You are young.")
        elif self.age>=13 and self.age<18:
            print ("You are a teenager.")
        else:
            print ("You are old.")
      
    def yearPasses(self):
        self.age += 1