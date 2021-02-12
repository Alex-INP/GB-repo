price_list = [22.3, 4.56, 64.53, 7.2, 74.68, 56, 2.33, 78, 177, 89.43, 12.83, 23.6, 43, 16.84, 29.7, 84.56, 234.53,
			  145.8, 1, 68.93]
# B
print("\n", "ID до: ", id(price_list), sep="")
price_list.sort()
print("Список отсортирован по возрастанию:")
print(price_list)
print("ID после:", id(price_list), "\n")

# C
reverse_pr_list = price_list.copy()
reverse_pr_list.reverse()
print("Список отсортирован по убыванию:")
print(reverse_pr_list, "\n")

# A
for ind, value in enumerate(price_list):
	if type(value) == float:
		rub, penny = str(value).split(".")
	else:
		rub, penny = value, 0
	price_list[ind] = f"{rub} руб {int(penny):02d} коп"
print("Преобразовано в строку:")
print(", ".join(price_list), "\n")

# D
five_goods = price_list[-5:]
print("Вывод по возрастанию пяти самых дорогих товаров в виде строки:")
print(", ".join(five_goods))
