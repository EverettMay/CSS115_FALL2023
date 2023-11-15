import random

class Course:

    def __init__(self, course_name, credit, grade):
        self.course_name = course_name
        self.credit = credit
        self.grade = grade

    def __str__(self):
        return f"{self.course_name} {self.credit} {self.grade}"

class Student:
    def __init__(self, name, email, major, project_info, letter_grade_to_GPA_dict):
        self.name = name
        self.email = email
        self.major = major
        self.project_info = project_info
        self.courses = []
        self.letter_grade_to_GPA_dict = letter_grade_to_GPA_dict
    
    def add_course(self, course):
        self.courses.append(course)
    
    def letter_grade_to_GPA(self, letter_grade):
        return self.letter_grade_to_GPA_dict[letter_grade]

    def calculate_GPA(self):
        total_credit = 0
        quality_points = 0
        for course in self.courses:
            total_credit += course.credit
            quality_points += course.credit * self.letter_grade_to_GPA(course.grade)
        return quality_points / total_credit

    def print_student_GPA(self):
        print(f"{self.name} {self.calculate_GPA()}")

def getInput():

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    major = input("Enter your major: ")
    project_info = input("Enter your project info: ")

    return name , email , major , project_info

    
def calculateGPA():
    Letter_Grade_to_GPA_dict = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0}

    student = Student(getInput(), Letter_Grade_to_GPA_dict)

    number_of_courses = int(input("Enter the number of courses: "))
    for i in range(number_of_courses):
        course_name = input("Enter the course name: ")
        credit = int(input("Enter the credit: "))
        grade = input("Enter the grade: ")
        student.add_course(Course(course_name, credit, grade))
        
    student.print_student_GPA()

def lotteryNumberGenerator():
    lottery_numbers = []
    for i in range(5):

        randomNumber = random.randint(0, 69)

        while(randomNumber in lottery_numbers):
            randomNumber = random.randint(0, 69)
        

        lottery_numbers.append(randomNumber)

    lottery_numbers.sort()
    lottery_numbers.append(random.randint(0, 26))
    print(*lottery_numbers, sep = " ")

def pigLatin():
    sentence = input("Enter a sentence: ").upper()
    sentenceList = sentence.split()
    for word in sentenceList:
        print(word[1:] + word[0] + "AY", end = " ")
    print()

def rockPaperScissors():

    list_of_choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice(rock, paper, or scissors): ")
    while user_choice not in list_of_choices:
        user_choice = input("Re-enter your choice: ")
    computer_choice = list_of_choices[random.randrange(0, 3)]
    print(f"You chose {user_choice} Computer chose {computer_choice}.")

    #If both players make the same choice, the game must be played again to determine the winner.
    if user_choice == computer_choice:
        print("Tie!")
        rockPaperScissors()
    #Rock beats scissors, scissors beats paper, and paper beats rock.
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
    

def main():
    print("1. Calculate Student GPA")
    print("2. Lottery Number Generator")
    print("3. Pig Latin")
    print("4. Rock, Paper, Scissors")
    print("9. Exit")

    choice = input("Enter your choice: ")
    choiceList = ["1", "2", "3", "4", "9"]

    while choice not in choiceList:
        choice = input("Re-enter your choice: ")

    while choice != "9":
        if choice == "1":
            calculateGPA()
        elif choice == "2":
            lotteryNumberGenerator()
        elif choice == "3":
            pigLatin()
        else:
            rockPaperScissors()

        print("1. Calculate Student GPA")
        print("2. Lottery Number Generator")
        print("3. Pig Latin")
        print("4. Rock, Paper, Scissors")
        print("9. Exit")

        choice = input("Enter your choice: ")
        while choice not in choiceList:
            choice = input("Re-enter your choice: ")

    print("Exit.")

if __name__ == "__main__":
    main()
    