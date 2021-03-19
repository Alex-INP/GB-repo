from abc import ABC, abstractmethod


class Clothes(ABC):
	@abstractmethod
	def get_calc(self):
		pass


class Fabric_Calc(Clothes):
	def __init__(self, size, formula):
		self.size = size
		self.formula = formula

	def __add__(self, other):
		return self.get_calc + other.get_calc

	@property
	def formula(self):
		return self.__formula

	@formula.setter
	def formula(self, formula):
		if formula == "Coat":
			self.__formula = self.size / 6.5 + 0.5
		elif formula == "Costume":
			self.__formula = 2 * self.size + 0.3

	@property
	def get_calc(self):
		return round(self.formula)


nc = Fabric_Calc(60, "Coat")
nc_2 = Fabric_Calc(60, "Costume")
print(nc.get_calc)
print(nc_2.get_calc)
print(nc + nc_2)
