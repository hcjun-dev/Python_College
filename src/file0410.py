## Hyungchol Jun
# 2014-04-10
# P_9.5

'''
implement a class SoadCan with methods getSurfaceArea() and getVolume(). In the constructor, supply the height and radius of the can
'''
from math import pi
from random import randint


class SodaCan(object):
	def __init__(self, height, radius):
		self._height = height
		self._radius = radius

	def getSurfaceArea(self):
		print("Surface Area is %.2f" % (2 * pi * (self._radius ** 2) + (2 * pi * self._radius * self._height)))

	def getVolume(self):
		print("Volume is %.2f" % (pi * (self._radius ** 2) * self._height))


def func0410():
	defaultCan = SodaCan(randint(1, 100), randint(1, 100))
	defaultCan.getSurfaceArea()
	defaultCan.getVolume()
