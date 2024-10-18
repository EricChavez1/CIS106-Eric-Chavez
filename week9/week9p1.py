def comnext(sales,month):
    if month in ['jan','feb','mar']:  
        return sales*1.10
    elif month in['apr','may','jun']:
        return sales*1.15
    elif month in ['jul','aug','sep']:
        return sales *1.20
    else:     
        return sales*1.25
    



r=input("Do you want to run program?'yes' or 'no' ")
while r=="yes":
    lname=input("Enter last name")
    sales=float(input("Enter Number of sales"))
    month = input("Enter Month:")
    newsale = comnext (sales,month)
    print("Last name:",lname)
    print("Next month's sales :",newsale)
    
    
    r=input("Do you want to run program again?'yes' or 'no' ")
    



