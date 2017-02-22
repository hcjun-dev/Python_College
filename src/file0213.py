# Hyungchol Jun
# 2014-02-12
# Average value calculating program
def func0213():
	count = 1
	loopQ = True
	average = 0
	stDeviation = 0
	sumv = 0
	sqSum = 0
	from math import sqrt
	inputv = input("Please input number: ")
	# start of while
	while loopQ == True:
		if inputv != "q":
			inputNum = int(inputv)
			# Sum calc
			sumv = sumv + inputNum
			sqSum = sqSum + inputNum ** 2
			# Average
			average = sumv / count
			# stDeviation area
			stDeviation = sqrt(((sqSum / count)) - (average ** 2))
			count = count + 1
			print("If you want to stop, input q.\n")
			inputv = input("Please input number: ")
			# Printing Zone
		else:
			if count > 1:
				loopQ = False
				print("\n==========Results====================================")
				print("You have put", count, "values")
				print("Your average of Values is", average)
				print("Your standard deviation of Values is", stDeviation)
			else:
				print("\n==========Results====================================")
				print("You have put", count, "values")
				print("Your average of Vlaues is", average)
				print("Your standard deviation of Values is 0")
