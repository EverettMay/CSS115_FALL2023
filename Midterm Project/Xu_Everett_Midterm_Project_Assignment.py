def roman_numerals(number):
		
def calc_population(starting_number, daily_increase, days):
	
def print_dict_to_table(user_dict):
	
if _name_ == "_main_":
	
	#Print info
	print("Everett Xu")
	print("yxx644@miami.edu")
	print("CSS115")
	print("Computer Science")

	while True:
		
		#Get user input number
		print("This Python program display Roman Numerals and Predict Population. Enter option 1 to display Roman Numerals. Enter option 2 to Predict Population. Enter 9 to Exit the program.")
		user_input = int(input())
	
		#Determine which option is chosen
		if user_input == 1:
			number = int(input("Enter the number you want to convert:"))
			print(f"The roman number is: {roman_numerals(number)}")
		elif user_input == 2:
			starting_number = int(input("Enter starting number of organism:"))
			daily_increase = int(input("Enter daily increase value(1-100):"))
			days = int(input("Enter number of days(2-30):"))
			population_dict = calc_population(starting_number, daily_increase, days)
			print_dict_to_table(population_dict)
		elif user_input == 9:
			break
		else:
			print("Invalid option")

