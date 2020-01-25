# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:56:04 2020

@author: Student
"""

matrix,matrix2=[],[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)        
 
matrix2==[[j for j in range(5)]for i in range(5)]       
