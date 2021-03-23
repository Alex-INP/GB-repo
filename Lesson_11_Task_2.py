class MyEx(Exception):
	def __init__(self, txt):
		self.txt = txt


def divi(a, b):
	if b == 0:
		raise MyEx(f"Деление на ноль: {a} / {b}.")
	return a / b

try:
	divi(4, 0)
except MyEx as e:
	print(f"Ошибка!\n{e}")