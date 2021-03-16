import random


class Car:
	def __init__(self, is_police):
		self.speed = 50
		self.color = "Green"
		self.name = "Skoda"
		self.is_p = is_police

	def go(self):
		print(f"Машина {self.name} поехала!")

	def stop(self):
		print(f"Машина {self.name} остановилась.")

	def turn(self):
		print(f"Машина повернулась на следующее количество градусов: {random.randint(0, 90)}")

	def show_speed(self):
		print(f"Скорость - {self.speed}")


class TownCar(Car):
	def show_speed(self):
		if self.speed > 60:
			print("Превышение скорости в 60")
		else:
			print(f"Скорость - {self.speed}")


class SportCar(Car):
	pass


class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40:
			print("Превышение скорости в 40")
		else:
			print(f"Скорость - {self.speed}")


class PoliceCar(Car):
	def __init__(self, is_p):
		super().__init__(is_p)
		self.is_p = True


for cla in [TownCar(False), SportCar(False), WorkCar(False), PoliceCar(False)]:
	print(f"{cla.__class__.__name__}: Имя:{cla.name}, Цвет:{cla.color}, Полиция:{cla.is_p}")
	cla.show_speed()
	print("-" * 70)

Car(False).go()
Car(False).turn()
Car(False).stop()
