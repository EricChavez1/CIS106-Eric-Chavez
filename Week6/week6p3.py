go=input("Do you want to run this program?(Yes or No)")
count=0
while (go=='Yes'):
    

    Lname=input('Enter Last Name')
    Score1=int(input("Enter Exam Score 1:"))
    Score2=int(input("Enter Exam Score 2:"))
    avg=(Score1+Score2)/2
    print("Average Score",avg)
    print("Last Name",Lname)
    go=input("Do you want to run this program again?(Yes or No)")
    count+=1

print("Number of Students that Entered Data",count)