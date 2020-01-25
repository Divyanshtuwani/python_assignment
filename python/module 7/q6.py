# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:43:35 2020

@author: Student
"""
from Automob import Automobile

class car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
       Automobile.__init__(self,make,model,mileage,price) 
    def set_doors(self,doors):
        self.doors=doors
    def get_doors(self):
        return self.doors
    
class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drivetype):
        Automobile.__init__(self,make,model,mileage,price)
    def set_drivetype(self,drivetype):
        self.drivetype=drivetype
    def get_drivetype(self):
        return self.drivetype
    
class SUV(Automobile):
    def __init__(self,make,model,mileage,price,passcap):
        Automobile.__init__(self,make,model,mileage,price)
    def set_passcap(self,passcap):
        self.passcap=passcap
    def get_passcap(self):
        return self.passcap
     
c=car("maruti",800,50,200000,4)
c.set_doors(4)
print(c.get_doors())  
c.set_mileage(50)
print(c.get_mileage())        

t=Truck("Ashok leyland",2000,50,1000000,"self")
t.set_drivetype("self")
print(t.get_drivetype())  
t.set_mileage(50)
print(t.get_mileage())        


s=SUV("Mahindra",2400,40,1200000,9)
s.set_passcap(9)
print(s.get_passcap())  
s.set_mileage(40)
print(s.get_mileage())        