# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:54:19 2020

@author: Siddharth
"""

number = int(input("State a first number: "))
check = int(input("State a second number: "))

# if number % 4 == 0:
#     print("Multiple of four")
# elif number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")
    
if number % check == 0:
    print(f"{check} is a multiple of {number}")
else:
    print(f"{check} doesn't divide into {number}")
