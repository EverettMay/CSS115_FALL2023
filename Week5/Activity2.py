year = int(input("Enter the year you are born:"))
age = 2023 - year

if (age < 1):
	age+=1

print("Age:", age)

if (age <= 1):
	print('Infant')
elif (age <= 13):
	print('Child')
elif (age <= 20):
	print('Teenager')
elif (age <= 65):
	print('Adult')
else: 
	print('Senior')
