def area_of_rectangle(length, width):
    return length * width

def main():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = area_of_rectangle(length, width)
    print("The area of the rectangle is", area)

main()