def compute_assessed_value(county, market_value):
    if county == 'cook':
        assessed_percent = 0.90
    elif county == 'dupage':
        assessed_percent = 0.80
    elif county == 'mchenry':
        assessed_percent = 0.75
    elif county == 'kane':
        assessed_percent = 0.60
    else:
        assessed_percent = 0.70

    assessed_value = market_value * assessed_percent
    return assessed_value

total_market_value = 0
total_assessed_value = 0

r = input("Do you want to enter a home? 'yes' or 'no': ")
while r == 'yes':
    county = input("Enter the county of the home: ")
    market_value = float(input("Enter the market value of the home: "))

    assessed_value = compute_assessed_value(county, market_value)

    total_market_value += market_value
    total_assessed_value += assessed_value

    print("County: ",county)
    print("Market value: $",market_value)
    print("Assessed value: $",assessed_value)

    r = input("Do you want to enter another home? 'yes' or 'no': ")

print("Total market value of all homes: $",total_market_value)
print("Total assessed value of all homes: $",total_assessed_value)
