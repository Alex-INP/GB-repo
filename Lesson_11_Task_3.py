class MyEx(Exception):
	def __init__(self, txt):
		self.txt = txt
num_list = []
while True:
	num = input("Bведите число: ")
	try:
		if num == "stop":
			print(num_list)
			break
		elif num.isdigit() and int(num) > 0:
			num_list.append(num)
		else:
			raise MyEx(f"не верный ввод: {num}")
	except MyEx as e:
		print(f"Ошибка!\n{e}")