def get_name():
    name = input("Please enter your name: ")
    return name

def get_major():
    major = input("Please enter your major: ")
    return major

def get_gpa():
    gpa = float(input("Please enter your GPA: "))
    return gpa

def get_contact_email():
    contact_email = input("Please enter your contact email: ")
    return contact_email

def is_valid(score):
    if score >= 0 and score <= 100:
        return True
    else:
        return False

def getAverage(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    return average

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_average_and_letter_grade(scores):
    average = getAverage(scores)
    letter_grade = get_letter_grade(average)
    return average, letter_grade

def getExamScores():
    scores = []
    number_of_scores = int(input("How many exam scores do you want to enter? "))
    while number_of_scores < 1 or number_of_scores > 5:
        number_of_scores = int(input("Re-enter how many exam scores do you want to enter? "))
    for i in range(number_of_scores):
        score = int(input(f"Please enter the score for exam {i + 1}: "))
        while not is_valid(score):
            score = int(input(f"Please re-enter the score for exam {i + 1}: "))
        scores.append(score)
    return scores

def show_Student_Info_and_Grades(name, major, gpa, contact_email, scores, average, letterGrade):
    print("Student Information")
    print(f"Name: {name}")
    print(f"Major: {major}")
    print(f"GPA: {gpa:.2f}")
    print(f"Contact Email: {contact_email}")
    print("Exam Scores")
    for i in range(len(scores)):
        print(f"Exam {i + 1}: {scores[i]}")
    average, letterGrade = get_average_and_letter_grade(scores)
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letterGrade}")

def main():
    name = get_name()
    major = get_major()
    gpa = get_gpa()
    contact_email = get_contact_email()
    scores = getExamScores()
    average, letter_grade = get_average_and_letter_grade(scores)
    show_Student_Info_and_Grades(name, major, gpa, contact_email, scores, average, letter_grade)

if __name__ == "__main__":
    main()