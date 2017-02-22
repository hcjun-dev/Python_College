# Hyungchol Jun
# 2014-02-24
# leapyear calculator

def func0225():
	# if year is miltiple of 4, 400 but not 100, return true, 100, false
	def leapyear(year):
		if year % 400 == 0:
			return True
		elif year % 100 == 0:
			return False
		elif year % 4 == 0:
			return True
		return 0

	# start of main function
	year = int(input("put the year you want"))
	if leapyear(year):
		print("%d is the leapyear" % year)
	elif not leapyear(year):
		print("%d is not the leapyear" % year)
	else:
		print("wrong input!")
