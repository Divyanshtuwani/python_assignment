# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:25:49 2020

@author: Student
"""

import pandas as pd
squad={"Batsman":{"Rohit Sharma":{"Matches":'206',"Runs":"8010","Average":"47.4","Highest_score":'264'},"Shikhar dhawan":{"Matches":'128',"Runs":"5355","Average":"44.4","Highest_score":'143'}
,"Virat Kohli":{"Matches":'227',"Runs":"10804","Average":"47.4","Highest_score":'183'}}}
c=[]
for i in squad.keys():
    for j in squad[i].keys():
     c.append(squad[i][j]["Highest_score"])
     
         
print("Max score:",max(c))
df=pd.DataFrame(squad['Batsman'])
print(df)