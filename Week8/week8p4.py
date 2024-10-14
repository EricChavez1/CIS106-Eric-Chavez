def compayrate (jobc):

    if jobc=='L':
        prate=25
    elif jobc=='A':
        prate=30
    else:
        prate=50 
    



        
    return prate



sum=0
r=input("Do you want to run program?'yes' or 'no' ")
while r=="yes":
    lname=input("Enter last name")
    hrs=float(input("Enter Number of Hours worked:"))
    jobc=input("Enter Job type(L,A,J):")
    
    prate=compayrate (jobc)
    if hrs > 40:
        overtime_hours = hrs - 40
        grossp = (40 * prate) + (overtime_hours * prate * 1.5)
    else:
        grossp = prate * hrs
    

    
    print("Last name:",lname)
    print("Hours worked:",hrs)
    print("gross pay:$",grossp)

    
    
    sum+=grossp#all gross pay
    r=input("Do you want to run program again?'yes' or 'no' ")

print("Total of all gross pay$:",sum)