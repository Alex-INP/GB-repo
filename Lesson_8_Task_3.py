def my_variable_decorator(visibility=0):
	def my_decorator(func):
		def my_wrapper(*args, **kwargs):
			arguments = *args, *kwargs.values()
			if visibility == 0:
				print(f'Декоратор полоучил от вас {visibility}, и вы ничего не получили.')
			if visibility == 1:
				print(f'Декоратор полоучил от вас {visibility}, и вы получили данные разделенные запятой:')
				print(*[type(i) for i in arguments], sep=", ")
			elif visibility == 2:
				print(f'Декоратор полоучил от вас {visibility}, и вы получили данные с максимальной детализацией:')
				for el in zip([i for i in arguments], [type(i) for i in arguments]):
					print(f'{func.__name__} ({el[0]} : {el[1]})')
			return func(*args, **kwargs)

		return my_wrapper

	return my_decorator


@my_variable_decorator(visibility=0)
def my_func(*args, **kwargs):
	print(f"\nJob done with arguments: {*args, *kwargs.values()}")


my_func("d", 4, False, {}, (), key=2.8, key_2="f")
