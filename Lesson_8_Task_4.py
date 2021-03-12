def my_callback_decorator(dec_arg):
	def my_decorator(func):
		def my_wrapper(arg):
			if not dec_arg(arg):
				raise ValueError(f'Wrong value: {arg}')
			return func(arg)

		return my_wrapper

	return my_decorator


@my_callback_decorator(lambda x: x <= 10)
def calc(x):
	return x ** x


print(calc(5))
print(calc(11))
