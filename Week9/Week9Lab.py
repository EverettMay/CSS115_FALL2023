def area_of_rectangle(length, width):
    return length * width

def showCelcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    print(f"The temperature in Celcius is {celcius:.2f}")

def main():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = area_of_rectangle(length, width)
    print("The area of the rectangle is", area)
    fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
    showCelcius(fahrenheit)

main()
