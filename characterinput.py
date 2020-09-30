# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:24:42 2020

@author: Siddharth
"""

name = input("What's your name? ")
age = int(input("How old are you? "))
year = str((2020-age)+100)
randomnum = int(input("Give us a random number: "))

for x in range(randomnum):
    print(f"Hey {name}, you'll be 100 years old in {year}\n")
