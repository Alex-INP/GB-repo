class Stationary:
	def __init__(self):
		self.title = self.__class__.__name__

	def draw(self):
		print(f"{self.title}: запуск отрисовки")


class Pen(Stationary):
	def draw(self):
		print(f"{self.title}: запуск отрисовки")


class Pencil(Stationary):
	def draw(self):
		print(f"{self.title}: запуск отрисовки")


class Handle(Stationary):
	def draw(self):
		print(f"{self.title}: запуск отрисовки")


Stationary().draw()
Pen().draw()
Pencil().draw()
Handle().draw()
