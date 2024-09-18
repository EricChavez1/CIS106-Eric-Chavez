#input
qty=int(input("Number of Ticktes"))
#process
if qty>= 25:
    unitprice=50
elif qty>= 10 and qty<=24:
    unitprice= 60
elif qty>= 5 and qty<=9:
    unitprice= 70
else:
    unitprice=75

total=qty*unitprice
#output
print("Number of ticktes:",qty)
print("Price per ticket:",unitprice)
print("Total Cost:      ",total)