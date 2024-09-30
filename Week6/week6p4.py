go=input("Do you want to run this program?(Yes or No)")
count=0
sum=0
while (go=='Yes'):
    

    Lname=input('Enter Last Name')
    hrs=int(input("Enter Hours Worked:"))
    rate=float (input("Enter Rate of pay:"))
    gros=hrs*rate
    if hrs>40:
       gros= ((hrs-40)*rate*1.5)+rate*40 
    else :gros==hrs*rate

    

    print("Gross pay",gros)
    print("Last Name",Lname)
    go=input("Do you want to run this program again?(Yes or No)")
    count+=1
    sum+=gros

print("Number of workers that Entered Data",count)
print("Sum of all gross pay: ",sum)
Avg=sum/count
print("Average pay",Avg)