def average(score1,score2,score3):
    avg=(score1+score2+score3)/3
    total=(score1+score2+score3)
    hcap=(total+handicap)/3
    return avg,hcap




lname=input("Enter last name")
score1=float(input("Enter score 1:"))
score2=float(input("Enter score 2:"))
score3=float(input("Enter score 3:"))
handicap=float(input("Enter Handicap:"))
avg,hcap=average(score1,score2,score3)

print("Last Name",lname)
print("Averaga handicap score",hcap)
print("Average Score",avg)