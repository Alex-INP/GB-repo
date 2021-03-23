class Orgtech:
	firm = "Hitachi"
	buyer = "Our IT Firm"


class Printer(Orgtech):
	def __init__(self, count):
		self.count = count
	color = "black"
	good_printing = False

class Scaner(Orgtech):
	def __init__(self, count):
		self.count = count
	color = "white"
	guarantee = {"year": 2, "month": 6}

class Xerox(Orgtech):
	def __init__(self, count):
		self.count = count
	color = "blue"
	who_asked_for_this = ["Bill", "Mag", "Mark"]

class OrgtechWarehouse:
	in_warehouse = {"Printer": Printer(0), "Scaner": Scaner(0), "Xerox": Xerox(0)}
	Design_department = {"Printer": Printer(0), "Scaner": Scaner(0), "Xerox": Xerox(0)}
	HR_department = {"Printer": Printer(0), "Scaner": Scaner(0), "Xerox": Xerox(0)}


	@classmethod
	def to_warehouse(cls, tech, num):
		try:
			if num <= 0 or type(num) == float:
				raise TypeError
			OrgtechWarehouse.in_warehouse[tech].count += num
		except TypeError:
			print("Нужно указать положительное числовое не дробное значение")

	@staticmethod
	def to_deps(what, from_where, to_where):
		try:
			from_where[what].count -= 1
			to_where[what].count += 1
		except KeyError as e:
			print(f"Такой инвентарь отсутствует: {e}\n")
		except NameError as e:
			print(f"Такой отдел отсутствует: {e}\n")

def show():
	print("In Warehouse - ", end="")
	for i in OrgtechWarehouse.in_warehouse:
		print(f"{i}: {OrgtechWarehouse.in_warehouse[i].count} ", end="")
	print("\nIn Design department - ", end="")
	for i in OrgtechWarehouse.Design_department:
		print(f"{i}: {OrgtechWarehouse.Design_department[i].count} ", end="")
	print("\nIn HR department - ", end="")
	for i in OrgtechWarehouse.HR_department:
		print(f"{i}: {OrgtechWarehouse.HR_department[i].count} ", end="")
	print("\n")


OrgtechWarehouse.to_warehouse("Printer", 5)
OrgtechWarehouse.to_warehouse("Scaner", 4)
OrgtechWarehouse.to_warehouse("Xerox", 3)

OrgtechWarehouse.to_warehouse("Xerox", -1)
OrgtechWarehouse.to_warehouse("Xerox", "fff")
OrgtechWarehouse.to_warehouse("Xerox", 3.5)


in_warehouse = OrgtechWarehouse.in_warehouse
Design_department = OrgtechWarehouse.Design_department
HR_department = OrgtechWarehouse.HR_department


show()
OrgtechWarehouse.to_deps("Printer", in_warehouse, Design_department)
show()
OrgtechWarehouse.to_deps("Printer", in_warehouse, HR_department)
show()
OrgtechWarehouse.to_deps("Xerox", in_warehouse, HR_department)
show()
OrgtechWarehouse.to_deps("Scaner", in_warehouse, HR_department)
OrgtechWarehouse.to_deps("Ser", in_warehouse, HR_department)
OrgtechWarehouse.to_deps("Scaner", in_warehouse, HR_department)
show()
OrgtechWarehouse.to_deps("Scaner", HR_department, Design_department)
show()

