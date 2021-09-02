# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:52:55 2021

@author: viraj
"""

list1 = [1,2,3,4,5,6,7]

print(list1)

print(list1[0])
print(list1[-1])



print(list1[1])
print(list1[-2])



print(list1[2])
print(list1[-3])

print(list1[3])
print(list1[-4])


print(list1[4])
print(list1[-5])


#OUTPUT

#[1, 2, 3, 4, 5, 6, 7]
#1
#7
#2
#6
#3
#5
#4
#4
#5
#3

lst = [[1,2,3,4],
       [1,2,3,4],
       [1,2,3,4],
       [1,2,3,4]]

print(lst)

#[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]


lst = [[[1,2,3], [4,5,6],[7,8,9]], 
       [[1,2,3], [4,5,6],[7,8,9]], 
       [[1,2,3], [4,5,6],[7,8,9]]]

print(lst)

print(lst[1:])

score = []

for i in lst:

  per = ((i[2] + i[3] + i[4] + i[5]) / 400)*100
  print(per)

  if (per < 100 and per > 90):
    grade = "A+"
  if (per < 89 and per > 79):
    grade = "A"
  if (per < 79 and per > 69):
    grade = "B+"
  if (per < 69 and per > 59):
    grade = "B"
  if (per < 59 and per > 49):
    grade = "F"

  score.append([i[0],i[1], per, grade])
  
  
#[[1, 'Rahul', 80.0, 'A'], [2, 'Jagrit', 78.5, 'B+'], [3, 'Roshan', 55.75, 'F']]