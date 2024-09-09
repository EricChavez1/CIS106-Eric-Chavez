#input 
make=input("Enter make")
model=input("Enter model")
msrp=float(input("Enter Msrp"))
discount=float(input("Enter discount"))
#process
amountoff=msrp*discount
discountedprice=msrp-amountoff


#Output
print("Make: ",make)
print("Model: ",model)
print("MSRP:$ ",msrp)
print("Discount percent %" ,discount)
print("Amount off:$ ",amountoff)
print("discounted price:$ ",discountedprice)