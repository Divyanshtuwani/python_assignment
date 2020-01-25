# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:50:14 2020

@author: Student
"""
people={ 1:{'name':'john','age':'27','sex':'male'},2:{'name':'marie','age':'22','sex':'Female'}}
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
people[3]={}
people[3]['name']='luna'
people[3]['age']='24'
people[3]['sex']='Female'
people[3]['married']='No'
print(people[3])
people[4]={'name': 'peter','age':'29','sex':'male','married':'yes'}

del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])