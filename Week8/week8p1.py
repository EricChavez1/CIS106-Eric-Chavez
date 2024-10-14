def compextprice(qty, unitprice):
    extprice=qty*unitprice
    if extprice >10000:
        discamt=extprice* .10
    else:
        discamt=0
    
    extprice=extprice-discamt
    return extprice
    
totalextprice=0
r= input("Do you want to run program? 'yes or no' ")

while r == "yes":
    qty=float(input("Enter Unit quantity"))
    unitprice=float(input("Enter unit price"))
    extprice=compextprice(qty,unitprice)
    totalextprice=totalextprice+extprice
    print("Extened price",extprice)
    
    r= input("Do you want to run program? 'yes or no' ")

print("Total Extened price",totalextprice)

