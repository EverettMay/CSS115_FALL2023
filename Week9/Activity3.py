def state_tax(amount):
    state_tax = (amount / 100) * 5
    return state_tax

def county_tax(amount):
    county_tax = (amount / 100) * 2.5
    return county_tax

def total(amount, stateTax, countyTax):
    total = amount + stateTax + countyTax
    return total

def main():
    amount = int(input("Enter the amount of a purchase: "))
    stateTax = state_tax(amount)
    countyTax = county_tax(amount)
    totalAmount = total(amount, stateTax, countyTax)
    print(f"The state tax is ${stateTax:.2f}")
    print(f"The county tax is ${countyTax:.2f}")
    print(f"The total is ${totalAmount:.2f}")

main()