#input 
numberofbooks=float(input("Number of Books:"))
costperbook=float(input("Cost per book:"))
#process
total=numberofbooks*costperbook
if total <= 50.00:
  shipping=25.00
else:
  shipping=0.00
total=numberofbooks*costperbook+shipping
#Output
print("Order Total:$",total)
print("Shipping Charge:$",shipping)