# This is a car class done in the 10:00 section of IT 210
"""
cost
stickerPrice
year
make
model
color
inv_number
"""


class Car:
	_invNumber = 1000  # Class Variable

	def __init__(self, make, model, year, cost):
		self._make = make
		self._model = model
		self._year = str(year)
		self._cost = cost
		Car._invNumber += 1
		self._invNum = Car._invNumber
		self._color = "Unknown"
		self._stickerPrice = cost * 1.3

	def getCost(self):
		return self._cost

	def getStickerPrice(self):
		return self._stickerPrice

	def getYear(self):
		return self._year

	def getMake(self):
		return self._make

	def setColor(self, color):
		self._color = color

	def setStickerPrice(self, price):
		self._stickerPrice = price

	def __repr__(self):
		s = "Inv# %d: %s %s %s" % (self._invNum, self._year,
		                           self._make, self._model)
		return s
