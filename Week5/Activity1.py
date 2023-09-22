scoreList = []
scoreList.append(int(input("Enter first exam score:")))
scoreList.append(int(input("Enter second exam score:")))
scoreList.append(int(input("Enter third exam score:")))
scoreList.append(int(input("Enter fourth exam score:")))

print("Original score list:", scoreList)

scoreList = [scoreList[0]*0.1, scoreList[1]*0.2, scoreList[2]*0.3, scoreList[3]*0.4]

sum = sum(scoreList)

print("Here;s weighted scores and sum of points:")
print("weighted score list", scoreList)
print("Total points:", sum)

if (sum >= 90):
	print("Letter grade is A")
elif (sum >= 80):
	print("Letter grade is B")
elif (sum >= 70):
	print("Letter grade is C")
elif (sum >= 60):
	print('Letter grade is D')
else:
	print("Letter grade is F")
