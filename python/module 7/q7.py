# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:20:04 2020

@author: Student
"""

class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return "Car color:"+self.color+" , "+"Mileage:"+self.mileage
        
c=Car("RED","60")        
print(c.__str__())