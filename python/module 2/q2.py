purchased=int(input("Enter the Number of packages purchased : "))
if purchased<10:
    dis=0
elif purchased<=19:
    dis=10/100*99
    
elif purchased<=49:
    dis=20/100*99
    
elif purchased<=99:
    dis=30/100*99
    
else:
    dis=40/100*99
print("amount of discount : ",dis)
print("Total amount is : ",99-dis)
