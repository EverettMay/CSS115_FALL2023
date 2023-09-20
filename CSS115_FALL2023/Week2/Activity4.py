quarters = int(input("Enter # of quarters:"))
dimes = int(input("Enter # of dimes:"))
nickels = int(input("Enter # of nickels:"))
pennies = int(input("Enter # of pennies:"))

dollars = (quarters*25+dimes*10+nickels*5+pennies*1)/100

print("You have", f'${dollars:.2f}')
