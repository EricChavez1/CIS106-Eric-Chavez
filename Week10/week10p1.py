def Discount(qty,price,discrate):
    total=qty*price
    discamt=total*discrate
    discprice=total-discamt
    return discamt,discprice








qty=float(input     ("Enter Quantity        :"))
price=float(input   ("Enter Price           :"))
discrate=float(input("Enter Discount Rate   :"))
discamt,discprice=Discount(qty,price,discrate)

print("    Quantity    :",qty)
print("    Price       :",price)
print("Discount Amount :",discamt)
print("Discounted Price:",discprice)