class Worker:
	def __init__(self, name, surname, position, income):
		self.args = [name, surname, position, income]
		self._info = {"wage": income, "bonus": 5000}


class Position(Worker):
	def get_full_name(self):
		print(self.args[0], self.args[1])

	def get_total_income(self):
		sel = 0
		for i in self._info.values():
			sel += i
		print(sel)


Position("Alex", "A", "worker", 10000).get_total_income()
Position("Alex", "A", "worker", 10000).get_full_name()
