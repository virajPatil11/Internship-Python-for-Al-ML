# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:24:14 2021

@author: viraj
"""
import json
record = { 11602259 : {"name": "Hello" , "Pno": 1234, "cgpa" : 7.5},
           11602260 : {"name": "Rutik Patil", "Pno": 3452, "cgpa" : 8},
           11602261 : {"name": "Viraj patil"   , "Pno": 8984, "cgpa" : 7.8}}


x = 11602259
print(record[x]['name'])
print(record[x]['Pno'])
print(record[x]['cgpa'])



record[11602259]['Pno'] = 111

print(record)


record = { 11602259 : {"name": "Hello" , "Pno": 1234, "cgpa" : 7.5},
           11602260 : {"name": "Rutik Patil", "Pno": 3452, "cgpa" : 8},
           11602261 : {"name": "Viraj patil"   , "Pno": 8984, "cgpa" : 7.8}}

js = json.dumps(record)

print(record)

print(type(record))

fd = open("record.txt",'r')
txt = fd.read()

fd.close()
print(txt)


fd = open("record.txt",'w')
fd.write(js)
fd.close()

print(txt)

record = json.loads(txt)
print(record)


import time
print(time.ctime())
