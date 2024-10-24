total=0.0
tax=0.0
def comtotal(qty,unitp):
    global total
    total=qty*unitp
    global tax
    tax=total*.07
    return 






qty=float(input("Quantity:"))
unitp=float(input("Unit Price"))
comtotal(qty,unitp)
print("Total:",total)
print("Tax:",tax)
