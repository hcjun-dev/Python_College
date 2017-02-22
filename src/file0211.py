# Hyungchol Jun
# 2014-02-10
def func0211():
	odd = 0
	even = 0
	sumv = 0
	inputT = True
	previousv = 0
	adjtimes = 0
	temp1 = 0
	temp2 = 0
	temp3 = 0
	temp4 = 0
	case1 = 0
	case2 = 0
	case3 = 0
	case4 = 0
	minv = 0
	maxv = 0
	adjv = []
	adjpop = []
	count = 1

	while inputT:
		print("============================================")
		print("1. Getting Smallest and Largest number.")
		print("2. Getting numbers of odd, and even inputs.")
		print("3. Getting cumulative total.")
		print("4. Getting adjacent duplicates.")
		print("0. To Quit, input 0.\n")
		inputvt = input("input the value you want: ")
		if inputvt == "1" or "2" or "3" or "4" or "0":
			inputv = int(inputvt)
			if inputv == 1:
				tmp = True
				case1 = input("Please input number:\n\n")
				while tmp == True:
					if temp1 == 0:
						minv = maxv = int(case1)

					if case1 == "":
						print("Wrong Input.")
						print("press q if you want to exit.")
						case1 = input("Please input number:\n\n")
					elif case1.isdigit() or ((case1[0] == "-") and (case1[1].isdigit())):
						number = int(case1)
						if minv <= number:
							minv = minv
						else:
							minv = number
						if maxv >= number:
							maxv = maxv
						else:
							maxv = number
						print("press q if you want to exit.")
						case1 = input("Please input number:\n\n")
						temp1 = temp1 + 1
					elif case1 == ("q"):
						tmp = False
						print("\n***result***")
						print("Minimum value so far was", minv)
						print("Maximum value so far was", maxv)
						print("\n\n")
						temp1 = 0
					else:
						print("Wrong Input.")
						print("press q if you want to exit.")
						case1 = input("Please input number:\n\n")
			elif inputv == 2:
				tmp = True
				case2 = input("Please input number:\n\n")
				while tmp == True:
					if (case2 == ""):
						print("Wrong Input.")
						print("press q if you want to exit.")
						case2 = input("Please input number:\n\n")
					elif (case2[0] == "-") or (case2 == "0"):
						print("please input positive values only.")
						print("press q if you want to exit.")
						case2 = input("Please input number:\n\n")
					elif case2.isdigit():
						number = int(case2)
						if number % 2 == 1:
							odd = odd + 1
						elif number % 2 == 0:
							even = even + 1
						else:
							continue
						print("press q if you want to exit.")
						case2 = input("Please input number:\n\n")
					elif case2 == ("q"):
						tmp = False
						print("\n***result***")
						print("Odd numbers were", odd, "times")
						print("Even numbers were", even, "times")
						print("\n\n")
						odd = 0
						even = 0
					else:
						print("Wrong Input.")
						print("press q if you want to exit.")
						case2 = input("Please input number:\n\n")
			elif inputv == 3:
				tmp = True
				case3 = input("Please input number:\n\n")
				while tmp == True:
					if case3.isdigit():
						if ((case3[0] == "-") and (case3[1].isdigit())) or case3.isdigit():
							number = int(case3)
							sumv = sumv + number
							print("The cumulative sum so far is", sumv)
							print("press q if you want to exit.")
							case3 = input("Please input number:\n\n")
						else:
							print("Wrong Input.")
							print("press q if you want to exit.")
							case3 = input("Please input number:\n\n")
					elif case3 == ("q"):
						tmp = False
						sumv = 0
					else:
						print("Wrong Input.")
						print("press q if you want to exit.")
						case3 = input("Please input number:\n\n")

			elif inputv == 4:
				tmp = True
				case4 = input("Please input number:\n\n")
				while tmp == True:
					if case4.isdigit():
						if ((case4[0] == "-") and (case4[1].isdigit())) or case4.isdigit():
							number = int(case4)
							if previousv == number:
								adjtimes = adjtimes + 1
								print("The value", number, "is adjacent for", adjtimes, "times")
							else:
								adjtimes = 0
								previousv = number

							print("press q if you want to exit.")
							case4 = input("Please input number:\n\n")
						else:
							print("Wrong Input.")
							print("press q if you want to exit.")
							case4 = input("Please input number:\n\n")
					elif case4 == ("q"):
						tmp = False
						adjtimes = 0
						previousv = 0

					else:
						print("Wrong Input.")
						print("press q if you want to exit.")
						case4 = input("Please input number:\n\n")
			elif inputv == 0:
				inputT = False
				print("End of Program")
			else:
				print("Error")
		else:
			print("Input Error")
