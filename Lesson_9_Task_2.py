class Road:
	def __init__(self, mass, layers):
		self._length = 5000
		self._width = 20
		self.m = mass
		self.la = layers

	def calc(self):
		print(f"{int((self._length * self._width * self.m * self.la) / 1000)}т.")


Road(25, 5).calc()
