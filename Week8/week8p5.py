def comtuition(credhrs, discode):
    if discode=='I':  
        return credhrs*250
    elif discode=='O':  
        return credhrs*550
    

sum=0
# in loop count+=1
r=input("Do you want to run program?'yes' or 'no' ")
while r=="yes":
    lname=input("Enter last name")
    credhrs=float(input("Enter Number credit hours"))
    discode = input("Enter 'I' for indistrict, or 'O'for out of district")
    owed = comtuition(credhrs,discode)
    print("Last name:",lname)
    print("Tuition owed:",owed)
    
    
    r=input("Do you want to run program again?'yes' or 'no' ")
    sum+=owed



print("Sum of all tuition owed ",sum)