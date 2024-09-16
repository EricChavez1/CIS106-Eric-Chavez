#input
appliance=input("Name of appliance")
cost=float(input("Cost"))

#process

if cost<=1000:
  percent=.05
else:
  percent=.10
waranty=cost*percent
#output
print("Appliance:",appliance)
print("Cost of Apliance;$",cost)
print("Waranty Cost:$",waranty)
print("Total;$",cost+waranty)
