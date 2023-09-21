#The function that convert number to roman number
def roman_numerals(number):
	#List the set of roman numbers
	roman_numbers = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
	#Use the input - 1 to find the right number
	return roman_numbers[number-1]


#The function for calculating popolation 
def calc_population(starting_number, daily_increase, days):
	#Create a empty dictionary for population
	population = dict()
	#Iterate the days given
	for i in range(1, days+1):
		#Set the day to the key and the population to the value
		#Calculate population with initial population times daily increase to the power of days - 1
		population[i] = starting_number * (1 + daily_increase / 100) ** (i - 1)
	#Return the population dictionary
	return population

#Function to print dictinary to a table for readability
def print_dict_to_table(user_dict):
	print("{:<10} {:<10}".format('Days', 'Population'))
	for key, value in user_dict.items():
		print("{:<10} {:<10}".format(key, value))
	
if __name__ == "__main__":
	
	#Print info
	print("Everett Xu")
	print("yxx644@miami.edu")
	print("CSS115")
	print("Computer Science")

	while True:
		#Get user input number
		print("This Python program display Roman Numerals and Predict Population. Enter option 1 to display Roman Numerals. Enter option 2 to Predict Population. Enter 9 to Exit the program.")
		user_input = int(input("Enter option:"))
		#Determine which option is chosen
		if user_input == 1:
			#If 1 is chosen, print the roman numebr given by roman_numerals()
			number = int(input("Enter the number you want to convert(1-10):"))
			#Check invalid input
			if number > 10 or number < 1:
				print("Invalid input")
				continue
			print(f"The roman number is: {roman_numerals(number)}")
		# If 2 is chosen 
		elif user_input == 2:
			#Take input for initial population, daily increase, and days
			starting_number = int(input("Enter starting number of organism:"))
			daily_increase = int(input("Enter daily increase value(1-100):"))
			days = int(input("Enter number of days(2-30):"))
			#Check invalid input
			if starting_number < 0:
				print("Invalid input")
				continue
			if daily_increase > 100 or daily_increase < 1:
				print("Invalid Input")
				continue
			if daily_increase < 2 or days > 30:
				print("Invalid input")
				continue
			#User calc_population() function to find the population and print in a table
			population_dict = calc_population(starting_number, daily_increase, days)
			print_dict_to_table(population_dict)
		#End loop if 9 is chosen
		elif user_input == 9:
			break
		#Check invalid input
		else:
			print("Invalid option")

