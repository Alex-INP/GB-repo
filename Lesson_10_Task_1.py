from itertools import zip_longest


class Matrix:
	def __init__(self, matr):
		self.matrix = matr

	def __str__(self):
		for i in self.matrix:
			print(("{} " * len(i)).format(*i))
		return ""

	def __add__(self, other):
		new_matrix = []
		try:
			for i in zip_longest(self.matrix, other.matrix, fillvalue=[]):
				new_matrix.append([sum(el) for el in zip_longest(i[0], i[1], fillvalue=0)])
			return Matrix(new_matrix)
		except(TypeError):
			print(f"Обнаружен не верный формат данных при сложении.\nВ матрицах:\n{self.matrix}\nи\n{other.matrix}")


matrix_1 = Matrix([[1, 2], [3, 8], [5, 6], [1]])
matrix_2 = Matrix([[7, 8], [10, 11, 3], [11, 12, 18, 4], [33, 32]])
print(matrix_1 + matrix_2)

matrix_5 = Matrix([[1, 2], [3, "r"], [5, 6]])
matrix_6 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix_5 + matrix_6)
