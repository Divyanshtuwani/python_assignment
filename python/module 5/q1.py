# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:28:05 2020

@author: Student
"""
def main():
 f=open('philosopher.txt','w')
 f.write('John Locke\n')
 f.write('David Hume\n')
 f.write('Edmund Burke\n')
 f=open('philosopher.txt','r')
 print(f.read())
main() 

def main1():
    f=open('philosopher.txt','w')
    f.write('10\n')
    f.write('20\n')
    f.write('30\n')
    f=open('philosopher.txt','r')
    line=f.readline()
    while line !="":  
     amount=float(line)
     line=f.readline()
     print(amount)
main1()    