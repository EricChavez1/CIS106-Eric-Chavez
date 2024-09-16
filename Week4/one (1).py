#input
itemquant=float(input("Item quantity:"))
#process

if itemquant>=1000:
  unitprice=3.00
else:
  unitprice=5.00
extendedprice = itemquant*unitprice
tax=extendedprice*.07
total=extendedprice+tax
#output
print("Extended Price:$",extendedprice)
print("Tax:$ ",tax)
print("Unit price$: ",unitprice)
print("Item quantity: ",itemquant)
print("Total:$ ",total)