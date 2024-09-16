#input
item=input("Enter Item")
quantity=float(input("Enter Quantity"))
#process

if item=="A":
  unitprice=10.00
else:
  unitprice=20.00
extenedprice=quantity*unitprice
#output
print("Item:",item)
print("Unit Price$:",unitprice)
print("Extended Price:$", extenedprice)