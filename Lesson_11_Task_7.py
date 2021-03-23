class Complex:
	def __init__(self, n_1, n_2):
		self.num_list = [int(n_1), int(n_2[:-1])]
		print(self.num_list)

	def __add__(self, other):
		sign = "+"
		if self.num_list[1] - other.num_list[1] < 0:
			sign = ""
		print(f"{self.num_list[0] - other.num_list[0]}{sign}{self.num_list[1] - other.num_list[1]}i")

	def __mul__(self, other):
		sign = "+"
		if self.num_list[0] * other.num_list[1] + other.num_list[0] * self.num_list[1] < 0:
			sign = ""
		print(
			f"{self.num_list[0] * other.num_list[0] + self.num_list[1] * other.num_list[1] * -1}{sign}"
			f"{self.num_list[0] * other.num_list[1] + other.num_list[0] * self.num_list[1]}i")


n_1 = Complex(5, "-6i")
n_2 = Complex(-3, "+2i")
n_1 + n_2
n_1 * n_2

n_3 = Complex(3, "+1i")
n_4 = Complex(2, "-3i")
n_3 * n_4
