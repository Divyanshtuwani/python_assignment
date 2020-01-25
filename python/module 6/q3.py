# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:37:26 2020

@author: Student
"""
import pickle

datastore={"office":{"medical":[{"room-number":100,"use":"reception","sq-ft":50,"price":75},{"room-number":101,"use":"waiting","sq-ft":250,"price":75},
                                {"room-number":102,"use":"examination","sq-ft":125,"price":150},{"room-number":103,"use":"examination","sq-ft":125,"price":150},
                                {"room-number":104,"use":"office","sq-ft":150,"price":100}],"Parking":{"location":"premium","style":"covered","price":750 }}}
file=open('datastore.dat','wb')
pickle.dump(datastore,file)
file.close()

def chamount(datastore):
  count=0  
  while(True):
    try: 
     a=int(input("Enter amount to be changed:"))
     r=int(input("Enter room number:"))
     break
    except:
     pass  
  for x in range(0,5):
      if r==datastore["office"]["medical"][x]["room-number"]:
         datastore["office"]["medical"][x]["price"]=a
         break
      else:
         count=count+1
  if count==5:
      chamount(datastore)
  return datastore    
  


def delrm(datastore):
   count=0 
   while(True):
    try:  
     r=int(input("Enter room number:"))
     break
    except:
     pass 
   for x in range(0,5):
        if r==datastore["office"]["medical"][x]["room-number"]:
          del datastore["office"]["medical"][x]
          break
        else:
            count=count+1
   if count==5:
        delrm(datastore)      
   return(datastore)
print(delrm(datastore))

def adroom(datastore):
   while(True):
    try:  
     r=int(input("Enter room number:"))
     p=int(input("Enter price:"))
     break
    except:
     pass 
    u=input("Enter reception:")
    s=input("Enter size:")
    datastore["office"]["medical"].append([{"room-number":r,"use":u,"sq-ft":s,"price":p}])
    print(datastore)

