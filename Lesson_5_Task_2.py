# Задание 1
# def odd_nums(max):
# 	for num in range(1, max+1):
# 		if num % 2 != 0:
# 			yield num
#
#
# gen_var = odd_nums(15)
#
# print(next(gen_var))
# print(next(gen_var))
# print(next(gen_var))
# print(next(gen_var))
# print(next(gen_var))
# print(next(gen_var))
# print(next(gen_var))
# print(next(gen_var))


# Задание 2
#
# def odd_nums(max):
# 	return [num for num in range(1, max+1) if num % 2 != 0]
#
#
# gen_var = odd_nums(15)
# print(gen_var)

gen_var = (num for num in range(1, 16) if num % 2 != 0)

print(next(gen_var))
print(next(gen_var))
print(next(gen_var))
print(next(gen_var))
print(next(gen_var))
print(next(gen_var))
print(next(gen_var))
print(next(gen_var))
