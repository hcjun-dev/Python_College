# Hyungchol Jun
# 2014-02-02
# InOrderProgram

def func0205():
	a = int(input("Input the first value:"))
	b = int(input("Input the second value:"))
	c = int(input("Input the third value:"))

	if (a < b):
		if (b < c):
			print("", a, b, c, "in order")
		elif (b == c):
			print("", a, b, c, "in order")
		else:
			print("", a, b, c, "not in order")
	elif (a == b):
		print("", a, b, c, "in order")
	else:
		if (b < c):
			print("", a, b, c, "not in order")
		elif (b == c):
			print("", a, b, c, "in order")
		else:
			print("", a, b, c, "in order")
