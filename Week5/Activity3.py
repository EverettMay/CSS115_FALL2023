firstLength = int(input("enter length of the first rectangle:"))
firstWidth = int(input("enter width of the first rectangle:"))
secondLength = int(input("enter length of the second rectangle:"))
secondWidth = int(input("enter width of the second rectangle:"))

firstArea = firstLength*firstWidth
secondArea = secondLength*secondWidth

if (firstArea > secondArea):
	print("First rectangle is larger")
elif (firstArea < secondArea):
	print("Second rectangle is larger")
else:
	print("Area are equal")
