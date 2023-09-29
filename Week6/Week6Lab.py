# endNumber = int(input("Enter the ending number:"))

# while(endNumber <= 0):
#	endNumber = int(input("Re-enter end number:"))

# This is a infinite list!!
# number_list = [1, 2, 3]
# for i in number_list:
#	number_list.append(i)
#	print(number_list)


for eachRow in range(1,10):
	for eachCol in range(eachRow):
		print('*', end='')
	print()
