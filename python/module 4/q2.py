# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:04:17 2020

@author: Student
"""

matrix=[[1,2,3],[4,5,6],[7,8,9]]
flatten_matrix=[]
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
print('flatter matrix:',flatten_matrix)        

#optimize
fm=[val for sublist in matrix for val in sublist]
print(fm)

planets=[['Mercury','Venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','Pluto']]
planet=[['Mercury','Venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','Pluto']]
flatt_planets=[planet for sublist in planets for planet in sublist if len(planet)<6]
print(flatt_planets)