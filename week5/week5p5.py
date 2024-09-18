#input
lname=input("Enter Last Name:  ")
sal=int(input("Enter Salary:   "))
job=int(input("Enter Job Level:"))
#process
if job>=10:
    bonusr=.25
elif job>=5 and job<=9:
    bonusr=.20
else:
    bonusr=.10

bonus=sal*bonusr
#output 
print("Last name:",lname)
print("Bonus:",bonus)