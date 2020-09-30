# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:12:37 2020

@author: Siddharth
"""

def solve(arr, threshold):
    finalArr = []
    for num in arr:
        if num < threshold:
            finalArr.append(num)
    
    print(f"The numbers {finalArr} are less than {threshold} from the input array")

array = []

n = int(input("Enter number of elements: "))

for i in range(0, n): 
    ele = int(input()) 
  
    array.append(ele)
    
thresh = int(input("Input the cap number: "))
    
solve(array, thresh)
    
    
          