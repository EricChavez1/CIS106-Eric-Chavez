#input
qty=int(input("Quantity of widgets"))
if qty>10000 :
    unitprice=10.00
elif qty>5000 :
    unitprice=20.00
else:
    unitprice=30.00
#process
extendedprice=qty*unitprice
tax=extendedprice*.07
total=extendedprice+tax
#output
print("Extended Price:",extendedprice)
print("Tax:",tax)
print("Total:",total)