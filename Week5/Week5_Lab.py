# firstNumber = float(input("First number:"))
# secondNumber = float(input("Second number:"))

# if (firstNumber > secondNumber):
# 	print(firstNumber, '>', secondNumber)
# elif (firstNumber, '<', secondNumber):
# 	print(firstNumber, '<', secondNumber)
# else:
# 	print(firstNumber, '=', secondNumber)

# numberCredit = int(input("Enter the number of credit you completed:"))

# if (numberCredit < 120):
# 	print("You are not eligible")

# else:
#	GPA = float(input("Enter GPA:"))
	
#	if (GPA >= 3.0):
#		print("You are eligible.")
#	else:
#		print("You are not eligible.")

numberCredit = int(input("Enter the number of credit you completed:"))
GPA = float(input("Enter GPA:"))

if (numberCredit > 120 and GPA >3.0):
	print("You are eligible")
else:
	print("You are not eligible")

