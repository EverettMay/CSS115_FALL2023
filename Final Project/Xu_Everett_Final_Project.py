import random

#Course class
class Course:

    #constructor with course_name, credit, grade attributes
    def __init__(self, course_name, credit, grade):

        self.course_name = course_name
        self.credit = credit
        self.grade = grade

    #print course_name, credit, grade
    def __str__(self):

        return f"{self.course_name} {self.credit} {self.grade}"

#Student class
class Student:

    #constructor with name, email, major, project_info, letter_grade_to_GPA_dict attributes, and empty courses list
    def __init__(self, name, email, major, project_info):

        self.name = name
        self.email = email
        self.major = major
        self.project_info = project_info
        self.courses = []
        self.letter_grade_to_GPA_dict = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0}

    #add course to courses list
    def add_course(self, course):

        self.courses.append(course)

    #convert letter grade to GPA
    def letter_grade_to_GPA(self, letter_grade):

        return self.letter_grade_to_GPA_dict[letter_grade]

    #calculate GPA
    def calculate_GPA(self):

        #calculate total credit and quality points, and use them to calculate GPA
        total_credit = 0
        quality_points = 0
        for course in self.courses:
            total_credit += course.credit
            quality_points += course.credit * self.letter_grade_to_GPA(course.grade)
        return quality_points / total_credit

    #print student name, email, project_info, GPA, and courses
    def print_student_GPA(self):

        print(f"{self.name} {self.email} {self.project_info} {self.calculate_GPA()}")
        for course in self.courses:
            print(course)

#Get student information and course information from user in one line and split to four variables by comma
def getStudentInfo():

    #Get student information from user in one line and split to four variables by comma
    student_information = input("Enter name, email, major, project info (separate by comma):")
    information_list = student_information.split(',')
    name = information_list[0]
    email = information_list[1]
    major = information_list[2]
    project_info = information_list[3]

    return name, email, major, project_info

#Get course information from user in one line and split to three variables by comma
def getCourseInfo():

    #Get course information from user in one line and split to three variables by comma
    course_information = input("Enter course, credit, grade (separate by comma):")
    information_list = course_information.split(',')
    course = information_list[0]
    credit = information_list[1]
    grade = information_list[2]
    while grade not in ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D"]:
        grade = input("Re-enter grade: ")

    return course, credit, grade
    
#Calculate student GPA
def calculateGPA():

    name, email, major, project_info = getStudentInfo()
    student = Student(name, email, major, project_info)
    #Get number of courses from user and add courses to student
    number_of_courses = int(input("Enter the number of courses: "))
    while number_of_courses <= 2 or number_of_courses >= 6:
        number_of_courses = int(input("Re-enter the number of courses: "))
    #Add courses to student
    for i in range(number_of_courses):
        course, credit, grade = getCourseInfo()
        student.add_course(Course(course, float(credit), grade))
        
    student.print_student_GPA()

#Generate lottery numbers
def lotteryNumberGenerator():

    lottery_numbers = []
    for i in range(5):

        #Generate a random number between 0 and 69.
        randomNumber = random.randint(0, 69)
        #If the number is already in the list, generate a new number.
        while(randomNumber in lottery_numbers):
            randomNumber = random.randint(0, 69)
        
        lottery_numbers.append(randomNumber)
    #sort the list and add a random number between 0 and 26 to the end of the list.
    lottery_numbers.sort()
    lottery_numbers.append(random.randint(0, 26))
    print(*lottery_numbers, sep = " ")

#Convert sentence to pig latin
def pigLatin():

    sentence = input("Enter a sentence: ").upper()
    sentenceList = sentence.split()
    #For each word in the sentence, move the first letter to the end of the word and add "AY" to the end of the word.
    for word in sentenceList:
        print(word[1:] + word[0] + "AY", end = " ")
    print()

#Rock, Paper, Scissors game
def rockPaperScissors():

    #Take user input and generate a random choice for the computer.
    list_of_choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice(rock, paper, or scissors): ")
    while user_choice not in list_of_choices:
        user_choice = input("Re-enter your choice: ")
    computer_choice = list_of_choices[random.randrange(0, 3)]
    print(f"You chose {user_choice} Computer chose {computer_choice}.")

    #If both players make the same choice, the game must be played again to determine the winner.
    if user_choice == computer_choice:
        print("Tie! You have to play again.")
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
    #Ask user if they want to play again.
    play_again = input("Do you want to play again?(y/n)")
    if play_again == 'y':
        rockPaperScissors()
    

def main():

    #Print menu
    print("1. Calculate Student GPA")
    print("2. Lottery Number Generator")
    print("3. Pig Latin")
    print("4. Rock, Paper, Scissors")
    print("9. Exit")

    #Get user choice
    choice = input("Enter your choice: ")
    choiceList = ["1", "2", "3", "4", "9"]
    #If user input is not in choiceList, ask user to re-enter choice
    while choice not in choiceList:
        choice = input("Re-enter your choice: ")
    #execute the function based on user choice
    while choice != "9":
        if choice == "1":
            calculateGPA()
        elif choice == "2":
            lotteryNumberGenerator()
        elif choice == "3":
            pigLatin()
        else:
            rockPaperScissors()
        #Print menu
        print("1. Calculate Student GPA")
        print("2. Lottery Number Generator")
        print("3. Pig Latin")
        print("4. Rock, Paper, Scissors")
        print("9. Exit")
        #Get user choice again
        choice = input("Enter your choice: ")
        while choice not in choiceList:
            choice = input("Re-enter your choice: ")

    print("Exit.")


if __name__ == "__main__":

    main()
    