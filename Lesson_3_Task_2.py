translation = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
			   "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate_adv(eng_word):
	if eng_word.lower() in translation:
		if eng_word[0].isupper():
			return translation[eng_word.lower()].title()
		else:
			return translation[eng_word]


print(num_translate_adv(input("Введите числистельное от 1 до 10 которое хотели бы перевести: ")))
