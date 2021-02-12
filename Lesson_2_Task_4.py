original_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in original_list:
	name = list(i.split(" "))[-1]
	print("Привет,", name.capitalize())
