pnum = int(input("Enter a Pocket number : "))
pocket="NULL"
if pnum == 0:
    pocket = "Green"
elif pnum<=10:
    if pnum%2==0:
        pocket = "Black"
    else:
        pocket = "Red"
elif pnum<=18:
    if pnum%2==0:
        pocket = "Red"
    else:
        pocket = "Black"
elif pnum<=28:
    if pnum%2==0:
        pocket = "Black"
    else:
        pocket = "Red"
elif pnum<=36:
    if pnum%2==0:
        pocket = "Red"
    else:
        pocket = "Black"
else:
     print("ERROR")
        
print("number of pocket is",pnum)
print("color of pocket is",pocket)
