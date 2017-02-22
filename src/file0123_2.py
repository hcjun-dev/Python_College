# Gallon calculator
# Hyungchol Jun 2014-01-20
# ver 0.1
from math import sqrt

def func0123_2():
	print("=================")
	print("Gallon Calculator")
	print("=================")
	# input value
	userInput = input("input the gallons in the tank: ")
	gallonInput = float(userInput)
	userInput = input("input the efficiency in miles per gallon: ")
	effInput = float(userInput)
	userInput = input("input price of gas per gallon: ")
	priceInput = float(userInput)
	print("")
	print("")

	# calculate
	ans1 = priceInput * 100 / effInput
	ans2 = gallonInput * effInput

	# output
	print("You will need", ans1, "dollars to go 100 miles for gas")
	print("You can go", ans2, "miles with your gas in the tank")
