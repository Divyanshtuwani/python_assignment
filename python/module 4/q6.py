# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:30:34 2020

@author: Student
"""
n=int(input("Enter no. of elements:"))
l,ct=[],[]
for i in range(n):
   a=int(input())
   l.append(a)
l.sort()   
for i in range(n):
  count=1   
  c=l[i] 
  for j in range(n):
      if c==l[j] and j!=i:
          count=count+1;        
  ct.append(count)  
for i in range(n):
      for  j in range(i+1,n):
         if ct[j] > ct[i]:
           temp = l[i]
           l[i] = l[j]
           l[j] = temp
     
print(l)

