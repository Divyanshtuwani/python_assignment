# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:26:50 2020

@author: Student
"""


class contact:
    def __init__(self,name,phno,em):
        self.name=name
        self.phno=phno
        self.em=em
    def set_name(self,name):
        self.name=name
    def set_phno(self,phno):
        self.phno=phno
    def set_em(self,em):
        self.em=em
    def get_name(self,name):
        return self.name
    def get_ph(self,phno):
        return self.phno
    def get_email(self,em):
        return self.em
    def __str__(self):
        return self.name+" "+self.phno+" "+self.em

o=contact("Mayank",'12345678',"fdgdg")      
Cont={0:o}
def addc(Cont):
     i=len(Cont)
     nm=input("Enter name of user:")
     phno=input("Enter phno of user:")
     em=input("Enter email of user:")
     o=input("Enter object name:")
     Cont[i]=o
     o=contact(nm,phno,em)
     print(Cont)
     
def Show_value(Cont):
    d=input("Enter object name:")
    for i in Cont.values():
        if d==i:
            print(d)

Show_value(Cont)            
