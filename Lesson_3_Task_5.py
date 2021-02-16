from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number, unique_words=False):
	"""
	Create jokes

	:param number: desirable number of jokes.
	:param unique_words: default = False. Send True, if no word repeat desired.
	"""
	for i in range(number):
		noun, adv, adj = choice(nouns), choice(adverbs), choice(adjectives)
		if unique_words == True:
			nouns.remove(noun)
			adverbs.remove(adv)
			adjectives.remove(adj)
		print(f"{noun} {adv} {adj}")


get_jokes(number=4, unique_words=True)
