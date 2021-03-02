from sys import argv

with open("bakery.csv", "r+", encoding="utf-8") as f:
	n, line, value = argv
	seek_num = 0
	lines_len = 0
	for i in f:
		lines_len += 1
	f.seek(0)

	if lines_len < int(line):
		print(f"Запись {line} отсутствует в списке.")
	else:
		for _ in range(int(line) - 1):
			seek_num += len(f.readline()) + 1
		f.seek(seek_num)
		f.write(value)
