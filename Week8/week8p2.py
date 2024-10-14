def compbatavg (hit,atbat):
    batavg=hit/atbat
    return batavg

count=0
# in loop count+=1
r=input("Do you want to run program?'yes' or 'no' ")
while r=="yes":
    lname=input("Players last name")
    hit=float(input("Number of hits"))
    atbat=float(input("Number of atbats"))
    avg=compbatavg(hit,atbat)
    print("Player Last name",lname)
    print("Batting average",avg)
    count+=1
    r=input("Do you want to run program again?'yes' or 'no' ")


   
print("Number of players entered",count)
