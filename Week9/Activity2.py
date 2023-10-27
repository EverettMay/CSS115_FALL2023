def assessed_value(value):
    assessed_value = value * 0.6
    return assessed_value
def property_tax(assessed):
    property_tax = (assessed / 100) * 0.72
    return property_tax
def main():
    value = int(input("Enter the actual value of the property: "))
    assessed = assessed_value(value)
    tax = property_tax(assessed)
    print(f"The assessed value is ${assessed:.2f}")
    print(f"The property tax is ${tax:.2f}")

main()