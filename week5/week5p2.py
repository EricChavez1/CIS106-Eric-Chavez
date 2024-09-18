#input
partnum=int(input("Part Number"))
qty=int(input("Quantity"))
#process
if partnum==10 or partnum==10:
    unitprice=1.00
elif partnum==99:
    unitprice=2.00
elif partnum==80 or partnum==70:
    unitprice=3.00
else:
    unitprice=5.00

total=qty*unitprice
#output
print("Part Number:  ",partnum)
print("Cost per Unit:",unitprice)
print("Total Cost:   ",total)

