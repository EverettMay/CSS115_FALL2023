examScore = []
examScore.append(int(input("Exam 1 score:")))
examScore.append(int(input("Exam 2 score:")))
examScore.append(int(input("Exam 3 score:")))
examScore.append(int(input("Exam 4 score:")))

print(f"The average is: {sum(examScore) / 4 :.2f}")

examScore[0] *= 0.1
examScore[1] *= 0.2
examScore[2] *= 0.3
examScore[3] *= 0.4

print(f"Weighted score: {examScore}")
print(f"Total points: {sum(examScore)}")

