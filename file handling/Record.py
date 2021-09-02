# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:41:10 2021

@author: viraj
"""

fd = open("Recordd.txt", "a")


name = input("Enter your name: ")
roll = int(input("Enter roll no: "))
eng = int(input("English marks: "))
hin = int(input("Hindi marks: "))
math = int(input("Math marks: "))
sci = int(input("Science marks: "))

data = name + "," + str(roll) + "," + str(eng) + "," + str(hin) + "," + str(math) + "," + str(sci) + "\n"


fd.write(data)

fd.close()

print("Data Recorded in text file")

#////////   output ///////////

#Enter your name: Viraj

#Enter roll no: 78

#English marks: 86

#Hindi marks: 78

#Math marks: 56

#Science marks: 76
#Data Recorded in text file