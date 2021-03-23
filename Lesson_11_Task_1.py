class Date:
	def __init__(self, date):
		self.date = date
	@classmethod
	def date_to_int(cls, date):
		try:
			return [int(i) for i in date.split(".")]
		except ValueError as v:
			print(f"Ошибка ввода данных:\n{v}")
	@staticmethod
	def valid(int_list):
		if not 0 < int_list[0] < 31:
			print("Не верная дата")
		if not 1 < int_list[1] < 12:
			print("Не верный месяц")
		if not 1 < int_list[2] < 9999:
			print("Не верный год")



Date.date_to_int("01.0f.2011")

Date.valid(Date.date_to_int("05.09.2022"))

Date.valid(Date.date_to_int("43.03.2022"))
Date.valid(Date.date_to_int("05.44.2022"))
Date.valid(Date.date_to_int("05.07.10000"))