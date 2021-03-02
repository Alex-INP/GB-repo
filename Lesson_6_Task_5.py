from itertools import zip_longest
from sys import argv

users = []
hobbies = []
_, file_1, file_2, file_3 = argv

with open(file_1, encoding="utf-8") as f:
	for line in f:
		users.append(line.replace("\n", "").replace(",", " "))

with open(file_2, encoding="utf-8") as f:
	for line in f:
		hobbies.append(line.replace("\n","").replace(",",", "))

with open(file_3, "w", encoding="utf-8") as f:
	for el in zip_longest(users, hobbies, fillvalue=None):
		f.write(f"{el[0]}: {el[1]}\n")

print(users)
print(hobbies)

final = zip_longest(users, hobbies, fillvalue=None)
print(*final)