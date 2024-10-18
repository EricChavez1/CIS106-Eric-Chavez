
def compute_price(msrp, make, model, electric_code):
    
    if make.lower == 'honda' and model == 'accord':
        discount = 0.10
    elif make == 'toyota' and model() == 'rav4':
        discount = 0.15
    elif electric_code == 'y':
        discount = 0.30
    else:
        discount = 0.05

    discountedprice = msrp * (1 - discount)

    
    finalprice = discountedprice * 1.07

    return finalprice



totalmsrp = 0
totalsalesprice = 0

r = input("Do you want to enter a vehicle? 'yes' or 'no': ")
while r == 'yes':
    make = input("Enter the make of the vehicle: ")
    model = input("Enter the model of the vehicle: ")
    electric_code = input("Is this an electric vehicle? (Y or N): ")
    msrp = float(input("Enter the MSRP (sticker price) of the vehicle: "))

    finalprice = compute_price(msrp, make, model, electric_code)

    totalmsrp += msrp
    totalsalesprice += finalprice

    print("Make: ",make, "Model",model)
    print("MSRP:",msrp)
    print("Final out-the-door price after discount and tax: $",finalprice)

    r = input("Do you want to enter another vehicle? 'yes' or 'no': ")


print("Total MSRP of all vehicles: $",totalmsrp)

print("Total out-the-door sales price of all vehicles: ",totalsalesprice)
