# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:28:04 2020

@author: Student
"""

x=input()
c=x.split(",")
tm=int(c[1])+int(c[2])+int(c[3])+int(c[4])+int(c[5])
te=int(c[6])+int(c[7])+int(c[8])
p=((tm+te)*100)/590
print(c[0],"obtained",tm,"out of 500 in theory and",te,"marks out of 90 in practical and succesfully passed exam with",p,"% in aggregate. Many congradulatins to",c[0],"." )