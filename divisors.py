# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:28:41 2020

@author: Siddharth
"""

n = int(input("State a number: "))
listOfNum = list(range(1, n+1))
divisors = []

for elem in listOfNum:
    if n % elem == 0:
        divisors.append(elem)
        
print(divisors)