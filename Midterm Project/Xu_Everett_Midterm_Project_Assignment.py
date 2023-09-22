if __name__ == "__main__":
	
	#Print info
	print("Everett Xu")
	print("yxx644@miami.edu")
	print("CSS115")
	print("Computer Science")
	
	user_input = 0

	while user_input != 9:
		#Get user input number
		print("This Python program display Roman Numerals and Predict Population. Enter option 1 to display Roman Numerals. Enter option 2 to Predict Population. Enter 9 to Exit the program.")
		user_input = int(input("Enter option:"))
		
		#Determine which option is chosen
		if user_input == 1:
			#If 1 is chosen, print the roman numebr given by roman_numerals()
			number = int(input("Enter the number you want to convert(1-10):"))
			
			#Check invalid input
			while (number < 1 or number > 10):
				number = int(input("Reenter the number you want to convert(1-10):"))
			
			#Create a list of roman numbers 
			roman_numbers = ['Hi','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
			print(f"The roman number is: {roman_numbers[number]}")
			
		# If 2 is chosen 
		elif user_input == 2:
			#Take input for initial population, daily increase, and days
			starting_number = int(input("Enter starting number of organism:"))
			daily_increase = int(input("Enter daily increase value(1-100):"))
			days = int(input("Enter number of days(2-30):"))
			
			#Check invalid input
			while (starting_number < 0 or daily_increase > 100 or daily_increase <1 or days < 2 or days > 30):
				starting_number = int(input("Reenter starting number of organism:"))
				daily_increase = int(input("Reenter daily increase value(1-100):"))
				days = int(input("Reenter number of days(2-30):"))
				
			#Create a dictinary for population
			population = dict()
			
			#Set the day to the key and the population to the value
			for i in range(1, days+1):
			#Calculate population with initial population times daily increase to the power of days - 1
				population[i] = starting_number * (1 + daily_increase / 100) ** (i - 1)

			#Print the population in a table
			print("{:<10} {:<10}".format('Days', 'Population'))
			for key, value in population.items():
				print("{:<10} {:<10.2f}".format(key, value))
	
		#End loop if 9 is chosen
		elif user_input == 9:
			print("Exit porgram")
			continue

		#Check invalid input
		else:
			print("Invalid option")

