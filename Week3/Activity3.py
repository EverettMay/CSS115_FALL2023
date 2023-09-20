amount = float(input("Enter amount of purchase:"))
tax = amount*0.07

print(f"Amount of purchase is:${amount:.2f}")
print(f"Tax is:${tax:.2f}")
print(f"Total value is:${amount+tax:.2f}")
