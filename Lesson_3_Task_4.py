def value_creator(check_letter, *args):
	dict_to_return = {}
	val_list = []
	for i in args:
		if i.split(" ")[1][0] == check_letter:
			val_list.append(i)

	for i in val_list:
		key = i.split(" ")[0][0]
		dict_to_return[key] = dict_to_return.setdefault(key, [])
		dict_to_return[key] = dict_to_return.get(key) + [i]
		# Вариант ниже тоже работает, но pycharm в этом случае почему-то подсвечивает 'setdefault',но почему именно не совсем понимаю.
		# dict_to_return[key] = dict_to_return.setdefault(key, []) + [i]
	return dict_to_return


def thesaurus_adv(*args):
	dict_to_return = {}

	for i in args:
		external_key = i.split(" ")[1][0]
		dict_to_return[external_key] = dict_to_return.setdefault(external_key, {})
		dict_to_return.get(external_key).update(value_creator(external_key, *args))
	return dict_to_return


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
