# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:50:44 2021

@author: viraj
"""

fd = open('Recordd.txt','a')


name = input("Enter the name: ")
roll_no = int(input("Enter the roll_no: "))
hindi = int(input("Enter marks in hindi: "))
eng = int(input("Enter marks in eng: "))
sci = int(input("Enter marks in sci: "))

data = name + "," + str(roll_no) + "," + str(hindi) + "," + str(eng) + "," + str(sci) + "\n"

fd.write(data)

fd.close()