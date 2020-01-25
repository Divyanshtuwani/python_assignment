# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:43:12 2020

@author: Student
"""

people={ 1:{'name':'john','age':'27','sex':'male'},2:{'name':'marie','age':'22','sex':'Female'}}
for p_id,p_info in people.items():
    print("\nPerson ID:",p_id)
    for key in p_info:
     print(key + ':',p_info[key])