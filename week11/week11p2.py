



lnames = ["chavez", "mordoc", "mclovin", "jones", "obama", "clinton", "biden", "trump", "kamala", "kennedy"]
scores = [85, 78, 92, 88, 76, 95, 80, 73, 91, 89]  

def displayar(lname, score):
    for i in range(0, len(lname)):  
        print(f"{lname[i]}: {score[i]}")  
 
displayar(lnames, scores)