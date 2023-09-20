schoolName = "University of Miami"

print(schoolName)
print(schoolName.upper())
print(schoolName[0])
print(len(schoolName))
print(schoolName[len(schoolName)-1])
print(schoolName[-1])


myStudents = "a b c d g i e"
myStudentsList = myStudents.split()

print(myStudentsList)
print(*myStudentsList)
print(*myStudentsList, sep=',')

myInfo = ["Everett", 19, 4.0]
myInfo.append("Computer Science")

print(*sorted(myStudentsList, reverse = True))

myList = [1, 2, 3]*2
myEvenNumberList = list(range(2, 10, 2))

print(myList)
print(myEvenNumberList)

