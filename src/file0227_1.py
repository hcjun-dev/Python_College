##
# Hyungchol Jun
# 2014-02-25
# P5.34 - laboratory container V and S

# importing pi and sqrt from math
import math


def func0227_1():
	def volume(R1, R2, h):
		V = (1 / 3) * math.pi * h * ((R1 ** 2) + (R2 ** 2) + R1 * R2)
		return V

	def surArea(R1, R2, h):
		S = math.pi * (R1 + R2) * math.sqrt((R2 - R1) ** 2 + (h ** 2)) + math.pi * (R1 ** 2)
		return S

	# start of main func.
	R1 = float(input("Please input R1 value: "))
	R2 = float(input("Please input R2 value: "))
	h = float(input("Please input height value: "))

	print("")
	print(volume(R1, R2, h), "cm^3 is the volume of the laboratory container")
	print(surArea(R1, R2, h), "cm^2 is the surface area of the laboratory container")
