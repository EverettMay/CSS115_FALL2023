import matplotlib.pyplot as plt

if __name__ == "__main__":
	
	#Print info
	print("Everett Xu")
	print("yxx644@miami.edu")
	print("CSS115")
	print("Computer Science")
	
	user_input = ' '

	while user_input != '9':
		
		#Get user input number	
		print("This Python program display Roman Numerals and Predict Population. Enter option 1 to display Roman Numerals. Enter option 2 to Predict Population. Enter 9 to Exit the program.")
			
		user_input = input("Enter option:")
		
		#Check for invalid input
		while (not user_input.isdigit() or user_input != '1' and user_input != '2' and user_input != '9'):
			user_input = input("Re-enter the option:")
		
		#Determine which option is chosen
		if user_input == '1':
			
			#If 1 is chosen, print the roman numebr given by roman_numerals()
			number = int(input("Enter the number you want to convert(1-10):"))
			
			#Check invalid input
			while (number < 1 or number > 10):
				number = int(input("Reenter the number you want to convert(1-10):"))
			
			#Create a list of roman numbers 
			roman_numbers = ['None','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
			print(f"The roman number is: {roman_numbers[number]}")
			
		# If 2 is chosen 
		elif user_input == '2':
			
			#Take input for initial population
			starting_number = int(input("Enter starting number of organism:"))
			
			#Check invalid input
			while (starting_number < 0):
				starting_number = int(input("Re-enter starting number of organism:"))
	
			#Take input for daily increase
			daily_increase = int(input("Enter daily increase value(1-100):"))
			
			#Check invalid input
			while (daily_increase > 100 or daily_increase <1):
				daily_increase = int(input("Re-enter daily increase value(1-100):"))
				
			#Take input for days
			days = int(input("Enter number of days(2-30):"))
			
			#Check invalid input
			while (days < 2 or days > 30):
				days = int(input("Re-enter number of days(2-30):"))
				
			#Create a dictinary for population
			population = dict()
			
			#Set the day to the key and the population to the value
			for i in range(1, days+1):
			#Calculate population with initial population times daily increase to the power of days - 1
				population[i] = starting_number * (1 + daily_increase / 100) ** (i - 1)

			#Print the population in a table for readability
			print("{:<10} {:<10}".format('Days', 'Population'))
			for key, value in population.items():
				print("{:<10} {:<10.2f}".format(key, value))

			x = list(map(int,population.keys()))
			y = list(map(int,population.values()))
			plt.plot(x,y)
			plt.xlabel("Days")
			plt.ylabel("Population")
			plt.show()
			
		#End loop if 9 is chosen
		elif user_input == '9':
			
			print("Exit porgram")
			continue


