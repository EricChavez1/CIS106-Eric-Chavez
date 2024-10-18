def computeticketprice(miles):
    if miles >= 30:
        return 12
    elif 20 <= miles <= 29:
        return 10
    elif 10 <= miles <= 19:
        return 8
    else:
        return 5

totalticketprice = 0

r = input("Do you want to purchase a ticket? 'yes' or 'no': ")
while r == 'yes':
    lastname = input("Enter your last name: ")
    miles = float(input("Enter the number of miles from downtown Chicago: "))

    ticketprice = computeticketprice(miles)

    totalticketprice += ticketprice

    print("Last name: ",lastname)
    print("Ticket price: $",ticketprice)

    r = input("Do you want to purchase another ticket? 'yes' or 'no': ")

print("Total price for all tickets: $",totalticketprice)
