# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:24:20 2020

@author: Student
"""

class con:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
       
o=con("mak")
def access(o):
  print(o.__str__())       
print(o) 
        