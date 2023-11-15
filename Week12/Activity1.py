def showInitials():
    name = input("Enter your name: ")
    name = name.split()
    initials = ""
    for i in name:
        initials += i[0]
        initials += "."
    print(initials.upper())

def showSum():
    numString = input("Enter a sequence of numbers with nothing separating them: ")
    total = 0
    for i in numString:
        total += int(i)
    print(total)

def showDate():
    date = input("Enter a date (mm/dd/yyyy): ")
    date = date.split("/")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December"]
    print(months[int(date[0]) - 1], date[1] + ",", date[2])

def main():
    showInitials()
    showSum()
    showDate()

if __name__ == "__main__":
    main()