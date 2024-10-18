def comsq2 (length,width,height):
    sq2=(2 * length * width) + (2 * length * height) + (2 * width * height)  
    return sq2


r=input("Do you want to run program?'yes' or 'no' ")
while r=="yes":
    
    length=float(input("Enter Length"))
    width=float(input("Enter Width"))
    height=float(input("Enter Height"))
    sq2=comsq2(length,width,height)
    print("Square Footage:",sq2)
    paint=sq2/50
    print("Number of gallons of paint needed",paint)
    
    r=input("Do you want to run program again?'yes' or 'no' ")


   
