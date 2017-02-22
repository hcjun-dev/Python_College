# Printing the rectangle's perimeter, and the diagnoal length.
# Hyungchol Jun 2014-01-20
# ver 0.2
from math import sqrt
def func0123_1():
	print("========================")
	print("")
	print("Rectangle calculator 0.2")
	print("")
	print("========================")
	userInput = input("Enter the longer length of rectangle: ")
	lengthOfSide1 = int(userInput)
	userInput = input("Enter the shorter length of rectangle: ")
	lengthOfSide2 = int(userInput)
	areaOfR = lengthOfSide1 * lengthOfSide2
	perimeterOfR = lengthOfSide1 * 2 + lengthOfSide2 * 2
	DiagOfR = sqrt(lengthOfSide1 ^ 2 + lengthOfSide2 ^ 2)
	print("")
	print("So the area of the Rectangle is : ", areaOfR)
	print("And the perimeter would be : ", perimeterOfR)
	print("Diagonal length of the rectangle is : ", DiagOfR)
