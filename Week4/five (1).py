#input
lname=input("Enter last name:")
dependents=float(input("Enter Number of Dependents:"))
income=float(input("Enter Gross Income:"))
#

adujstedgross=income-dependents*12000
if adujstedgross<=50000:
  taxperc=.10
else:
  taxperc=.20
incometax=taxperc*adujstedgross

if incometax<0:
    incometax=100
else:
    income=income
  
#output
print("Last Name:",lname)
print("Gross Income:$",income)
print("Number of Dependents:",dependents)
print("Adjust Gross Income:$",adujstedgross)
print("Income Tax:$", incometax)