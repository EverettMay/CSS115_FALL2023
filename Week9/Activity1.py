def kilometer_to_mile(kilometer):
    return kilometer * 0.621371

def main():
    kilometer = int(input("Enter the distance in kilometers: "))
    mile = kilometer_to_mile(kilometer)
    print(f"The distance in miles is {mile:.2f}")

main()