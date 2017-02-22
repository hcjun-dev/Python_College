# Hyungchol Jun
# 2014-01-27
def func0128():
	# Getting input in integer
	inputV1 = int(input("Input the first value:"))
	inputV2 = int(input("Input the second value:"))

	# Calculating
	sumV = inputV1 + inputV2
	differenceV = inputV1 - inputV2
	productV = inputV1 * inputV2
	averageV = (inputV1 + inputV2) / 2
	# Desciding what is bigger
	if inputV1 < inputV2:
		distanceV = inputV2 - inputV1
		maxV = inputV2
		minV = inputV1
	elif inputV1 > inputV2:
		distanceV = inputV1 - inputV2
		maxV = inputV1
		minV = inputV2
	else:
		distanceV = 0
		maxV = inputV1
		minV = inputV1

	# Print area
	print("The sum of the two would be", sumV)
	print("The difference of the two would be", differenceV)
	print("The product of the two would be", productV)
	print("The average of the two would be", averageV)
	print("The distance of the two would be", distanceV)
	print("The maximun value of two would be", maxV)
	print("The minimum of two would be", minV)
