import os
from os import path

last_len = 0
file_path = ""

with open("config.yaml", encoding="utf-8") as f:
	root_dir = f.readline()[f.readline().index("--"):].strip()
	f.seek(0)

	for line in f:
		prefix_len = len(line[:line.index("--")])
		name = line[line.index("--") + 2:].strip()

		if prefix_len > last_len:
			if "." in name:
				os.makedirs(file_path)
				open(path.join(file_path, name), "w").close()
			else:
				file_path = path.join(file_path, name)
			last_len = prefix_len

		elif prefix_len == last_len:
			if "." in name:
				if not path.exists(path.join(file_path, name)):
					open(path.join(file_path, name), "w").close()
			else:
				os.makedirs(path.join(file_path, name))
				file_path = path.join(file_path, name)
			last_len = prefix_len

		else:
			file_path = path.join(root_dir, name)
			last_len = prefix_len
