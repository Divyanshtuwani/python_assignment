# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:33:29 2020

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
def main():   
 c=contact("Mayank ppp",'90968567',"Mak@gmail.com")
 c.set_name("Mayank")    
 c.set_phno('90968567')            
 c.set_em("Mak@gmail.com")
 print(c.__str__())            
main()
 