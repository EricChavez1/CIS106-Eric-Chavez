def Report(sales):
    if sales>100000:
        comp=.10
    else: comp=.05
    com=sales*comp
    next=sales*1.05
    return next,com








lname=input("Enter last name")
sales=float(input("Enter Sale"))
next,com=Report(sales)
print("Last name",lname)
print("Commission",com)
print("Next Years Target:",next)
