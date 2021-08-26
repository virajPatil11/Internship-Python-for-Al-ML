# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:42:56 2021

@author: viraj
"""

num = input("Enter a number: ")

while (num != 0):
    print(num)
    num = num - 1;
    
num = input("Enter a number: ")

for i in range(num,0,-1):
    print(i)
    
num = 12
binary = ''

while (num != 0):
    
    if (num % 2 == 0):
        binary += '1'
    else:
        binary += '0'
    num = num / 2
    
    print(binary)