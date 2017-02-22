# Hyungchol Jun
# 2014-04-20
# 0421.py P_10.9

"""
Make a class Employee with a name and salary. Make a class Manager inherit from employee. Add an instance variable,
named _department, that sorts a string. Supply a method __repr__ that prints the manager's name, department,
and salary. Make a class Executive inherit from manager. Supply appropriate __repr__ methods for all classes.
Supply a test program that tests these classes and methods.
"""


class Employee:
	def __init__(self, name, salary):
		self._name = name
		self._salary = salary

	def getName(self):
		return self._name

	def getSalary(self):
		return self._salary

	def setName(self, new_name):
		self._name = new_name

	def setSalary(self, new_salary):
		self._salary = new_salary

	def __repr__(self):
		s = "Name: %s  Salary: %d" % (self._name, self._salary)
		return s


class Manager(Employee):
	_department = "Unknown"

	def __init__(self, name, department, salary):
		super().__init__(name, salary)
		self._department = department

	def getDepartment(self):
		return self._department

	def setDepartment(self, department):
		self._department = department

	def __repr__(self):
		p = "Name: %s  Department: %s  Salary: %d" % (self._name, self._department, self._salary)
		return p  # manager's name, department, and salary


class Executive(Manager):
	def __init__(self, name, department, salary):
		super().__init__(name, department, salary)

	def getDepartment(self):
		return self._department

	def setDepartment(self, department):
		self._department = department

	def __repr__(self):
		q = "Name: %s  Department: %s  Salary: %d" % (self._name, self._department, self._salary)
		return q

def func0421():
	if __name__ == "__main__":
		employee = []
		employee.append(Employee("Eric", 5000))
		employee.append(Manager("Ashley", "Sales", 5000))
		employee.append(Executive("Taylor", "Production", 10000))
		for emp in employee:
			print(emp)
