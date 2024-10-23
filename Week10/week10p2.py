def average(Exam1,Exam2,Exam3):
    avg=(Exam1+Exam2+Exam3)/3
    Totalp=Exam1+Exam2+Exam3
    return avg,Totalp




lname=input("Enter last name")
Exam1=float(input("Enter exam 1 score:"))
Exam2=float(input("Enter exam 2 score:"))
Exam3=float(input("Enter exam 3 score:"))

avg,Totalp=average(Exam1,Exam2,Exam3)

print("Last Name",lname)
print("Total Points",Totalp)
print("Average Exam Score",avg)
