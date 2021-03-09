import os
import json
from collections import defaultdict
from os import path

stat_dict = defaultdict(lambda: (0, []))
directory = input("Укажите путь: ")

for i in os.listdir(directory):
	if path.isfile(path.join(directory, i)):
		border = len(str(os.stat(path.join(directory, i)).st_size))
		stat_dict[10 ** border] = stat_dict[10 ** border][0] + 1, stat_dict[10 ** border][1]

		if i[i.index(".") + 1:] not in stat_dict[10 ** border][1]:
			stat_dict[10 ** border][1].append(i[i.index(".") + 1:])

with open("summary.json", "w", encoding="utf-8") as f:
	json.dump(stat_dict, f)
