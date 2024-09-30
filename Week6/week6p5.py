go=input("Do you want to run this program?(Yes or No)")
sumdisc=0
count=0
while (go=='Yes'):
    

    price=float(input('Enter Price of Item'))
    qty=float(input("Enter quantity:"))

    extprice=(price*qty)
    disc=extprice*.10
    if extprice>10000:
        disc=extprice*.25

    

    total=extprice-disc

    print("Extentnded price:",extprice)
    print("Discount amount:",disc)
    print("Total:",total)
    
    go=input("Do you want to run this program again?(Yes or No)")
    sumdisc+=disc
    count+=1
    
print("sum of all discounts:",sumdisc)