def isValid(score):
	while (score > 100 or score < 0):
		score = int(input("Re enter score from 0-100:"))
	return score

scoreList = []
scoreList.append(isValid(int(input("Enter first exam score:"))))
scoreList.append(isValid(int(input("Enter second exam score:"))))
scoreList.append(isValid(int(input("Enter third exam score:"))))


average = sum(scoreList)/3

print("Average points:", average)

if (average >= 90):
	print("Letter grade is A")
elif (average >= 80):
	print("Letter grade is B")
elif (average >= 70):
	print("Letter grade is C")
elif (average >= 60):
	print('Letter grade is D')
else:
	print("Letter grade is F")
