class Cell:
	def __init__(self, cell_number):
		self.cell_number = cell_number

	def __add__(self, other):
		return Cell(self.cell_number + other.cell_number)

	def __sub__(self, other):
		if self.cell_number >= other.cell_number:
			return Cell(self.cell_number - other.cell_number)
		else:
			return Cell(other.cell_number - self.cell_number)

	def __mul__(self, other):
		return Cell(self.cell_number * other.cell_number)

	def __floordiv__(self, other):
		if self.cell_number >= other.cell_number:
			return Cell(self.cell_number // other.cell_number)
		else:
			return Cell(other.cell_number // self.cell_number)

	def make_order(self, num):
		lines = int(self.cell_number / num)
		last_line = self.cell_number % num
		return ('{}' * num + "\n").format(*["*" for _ in range(num)]) * lines + \
			   ('{}' * last_line + "\n").format(*["*" for _ in range(last_line)])


cl = Cell(43)
cl_2 = Cell(56)
print(cl.make_order(7))

print((cl + cl_2).cell_number)
print((cl + cl_2).make_order(18))

print((cl - cl_2).cell_number)
print((cl - cl_2).make_order(5))

print((cl * cl_2).cell_number)
print("")
print((cl // cl_2).cell_number)
print((cl // cl_2).make_order(3))
