def commpg (milest,gall):
    mpg=milest/gall
    return mpg

count=0
# in loop count+=1
r=input("Do you want to run program?'yes' or 'no' ")
while r=="yes":
    city=input("Destination City")
    milest=float(input("Enter Number of miles driven"))
    gall=float(input("Enter amount of fuel used"))
    mpg=commpg(milest,gall)
    print("Destination city:",city)
    print("Miles:",milest)
    print("Miles per gallon",mpg)
    count+=1
    r=input("Do you want to run program again?'yes' or 'no' ")


   
print("Number of Entries made ",count)