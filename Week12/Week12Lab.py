def practice1():
    print(" *"*30)
    for eachRound in range(1, 11):
        print(" *"*eachRound)

def practice2():
    myString = "University of Miami"
    myFirstSubstring = myString[0:10]
    myThirdSubstring = myString[14:]
    print(myString)
    print(myFirstSubstring)
    print(myThirdSubstring)
    myStringList = myString.split()
    print(myStringList[0])

def practice3():
    studentList = ["John", "Mary", "Bob", "Jane", "Peter", "Susan"]
    studentGPAList = [3.5, 3.8, 2.9, 3.2, 3.9, 3.7]
    print(f"{'Student Name':<25}{'Student GPA':>15}")
    for eachRound in range(len(studentList)):
        print(f"{studentList[eachRound]:<25}{studentGPAList[eachRound]:>15}")

def main():
    print("WEEK 12 LAB")
    practice3()

if __name__ == "__main__":
    main()