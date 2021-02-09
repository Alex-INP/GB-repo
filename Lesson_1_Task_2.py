numbers_cube = []

for i in range(1, 1000, 2):
	numbers_cube.append(i ** 3)

print(numbers_cube)

final_summ = 0
for i in range(len(numbers_cube)):
	num = 0
	original_number = numbers_cube[i]

	while numbers_cube[i]:
		last_num = numbers_cube[i] % 10
		numbers_cube[i] //= 10
		num += last_num
	if num % 7 == 0:
		print("Сумма чисел числа", original_number, "делится на 7 без остатка")
		final_summ += original_number
	numbers_cube[i] = original_number

print("Итоговая сумма чисел: ", final_summ, "\n")

for i in range(len(numbers_cube)):
	numbers_cube[i] += 17

final_summ_17 = 0
for i in range(len(numbers_cube)):
	num = 0
	original_number = numbers_cube[i]

	while numbers_cube[i]:
		last_num = numbers_cube[i] % 10
		numbers_cube[i] //= 10
		num += last_num
	if num % 7 == 0:
		print("Сумма чисел числа", original_number, "делится на 7 без остатка")
		final_summ_17 += original_number
	numbers_cube[i] = original_number

print("Итоговая сумма чисел c +17: ", final_summ_17)

"""
for i, value in enumerate(numbers_cube):
	num = 0
	for n in str(value):
		num += int(n)
	if num % 7 == 0:
		print("Сумма чисел числа", value, "делится на 7 без остатка")
		final_summ += value
"""
