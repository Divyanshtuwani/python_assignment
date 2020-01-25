# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:16:28 2020

@author: Student
"""


f={"fruit":{"Name":["Apple","Mango","Papaya"],"Bionomical_Name":["malus_domestica","Mangifera indica","Carica papaya"],"Major_producers":["China","US","Turkey"],
            "Nutrition":{"carbohydrate":['13.80','45','67'],"Fat":['0.17','89','90'],"Protien":[0.2,65,212]}}}
for i in range(0,3):
    if f["fruit"]["Nutrition"]["Protien"][i]==max(f["fruit"]["Nutrition"]["Protien"]):
         x=f["fruit"]["Name"][i]
print(x)        
            
                
            