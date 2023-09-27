counter = 1
sum = 0
while(counter <= 10):
	sum += counter
	counter += 1
	
print(sum)


examScore = float(input("Enter exam score:"))

while (examScore>100 or examScore<0):
	examScore = float(input("Re-enter exam score:"))
