#input
prince=float(input("Enter priciple amount"))
mature=float(input("Enter years to maturity"))
#process
if prince>100000 and mature==5:
    interest=.06
elif prince>=50000 and prince<=100000 and mature==10:
    interest=.05
elif prince>=50000 and prince<=100000 and mature==5:
    interest=.04
else:
    interest=.02

itr=interest*100
fir=prince*interest
#output
print("Principle Amount:   ",prince)
print("Interest rate:      ",itr)
print("First Year Interest:",fir)