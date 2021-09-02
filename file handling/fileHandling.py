# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:36:15 2021

@author: viraj
"""

fd = open("text.txt", 'r')

print(fd.read())
fd.close()


fd = open("text.txt", "r")
txt = fd.read()
fd.close()


print(txt)
print(type(txt))

lines = txt.split(".")

print(len(lines))

x = txt.split("\n")

print(x)

print(x[0])