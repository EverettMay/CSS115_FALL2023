def isScoreValid(score):
	while (score > 100 or score < 0):
		score = int(input("Re enter score from 0-100:"))
	return score
def isStudentValid(student):
	while (student > 5 or student < 1):
		student = int(input("Re enter student from 1-5:"))
	return student
def isTestValid(test):
	while (test > 3 or test < 1):
		student = int(input("Re enter tests from 1-3:"))
	return test


numberStudent = isStudentValid(int(input("Enter number of student from 1-5:")))
numberTest = isTestValid(int(input("Enter number of test from 1-3:")))

for student in range(1,numberStudent+1):
	print("Enter scores for student", student)
	scores = []
	for test in range(1,numberTest+1):
		scores.append(isScoreValid(int(input(f"Enter score for test {test}:"))))
	print(f"Average is: {sum(scores)/numberTest:.2f}", )
		
