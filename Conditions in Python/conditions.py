# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:38:41 2021

@author: viraj
"""

age = -123;

print(age > 18);

if (age < 0):
    print('Please enter a valid age!')

elif (age >= 18 or age <= 120):
    print('You can vote!')  
    
else:
    print('You can not vote!')
    
drinks = True
maggie = False
coffee = True
water  = False
burger = True

orders = 0

if (drinks == True):
    print('Enjoy your drinks')
    orders += 1

if (maggie == True):
    print('Enjoy your Maggie')
    orders += 1
    
if (coffee == True):
    print('Enjoy your Coffee')
    orders += 1
    
if (water == True):
    print('Enjoy your water')
    orders += 1
    
if (burger == True):
    print('Enjoy your Burger')
    orders += 1