# Hyungchol Jun
# 2014-02-02
# DetectingDigitsAndletters
def func0206():
	s = input("Input the value:")
	if s.endswith("."):
		print("It ends with period")
	elif s.isdigit():
		print("It is only with digits")
	elif s.isalpha():
		if s.isupper():
			print("It is only with uppercase letters")
		elif s.islower():
			print("It is only with lowercase letters")
		else:
			if s[0].isupper():
				print("It starts with uppercase letter")
			else:
				print("Nothing matches")
	elif s.isalnum():
		print("It contains letters and digits")
	else:
		print("You have put the wrong thing")
