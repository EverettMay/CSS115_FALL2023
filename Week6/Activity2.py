
options = [1,2,3,4,9]
option = 0


while option != 9:
	print("Enter 1 to add")
	print("Enter 2 to subtract")
	print("Enter 3 to multiply")
	print("Enter 4 to divide")
	print("Enter 9 to exit")
	
	option = int(input("Enter option 1, 2, 3, 4, or 9:"))

	while option not in options:
		option = int(input("Re enter option 1, 2, 3, 4, or 9:"))
		
	if option == 1:
		print("Add")
	elif option == 2:
		print("Subtract")
	elif option == 3:
		print("Multply")
	elif option == 4:
		print("Divide")
	
