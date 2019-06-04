#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:27:00 2019

@author: sercangul
"""
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName,idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber      
        self.scores = scores 

    def calculate(self):
        average = sum(self.scores)/len(self.scores)    
        if average >= 90:
            result = "O"
        elif average >= 80:
            result = "E"
        elif average >= 70:
            result = "A"
        elif average >= 55:
            result = "P"
        elif average >= 40:
            result = "D"
        else:
            result = "T"
        return result

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())