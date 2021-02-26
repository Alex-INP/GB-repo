from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В']  # , '8Б', '10А', '10Б', '9А']


def tuto_klas_gen(tuto, klas):
	for i in range(len(tuto)):
		pair = list(zip_longest(tuto, klas, fillvalue=None))
		yield pair[i]


kort_gen = tuto_klas_gen(tutors, klasses)
print("Создан генератор:", kort_gen)
print(next(kort_gen))
print(next(kort_gen))
print(next(kort_gen))
print(next(kort_gen))
print(next(kort_gen))
print(next(kort_gen))
print(next(kort_gen))
print(next(kort_gen))  # Истощен
