from sys import argv

lines_len = 0
with open("bakery.csv", encoding="utf-8") as f:
	for i in f:
		lines_len += 1


def show_sales(start=1, end=lines_len):
	with open("bakery.csv", encoding="utf-8") as f:
		seek_num = 0
		for _ in range(start - 1):
			seek_num += len(f.readline())

		f.seek(seek_num + start - 1)
		for _ in range(end - start + 1):
			print(f.readline().strip())


if len(argv) == 1:
	show_sales()
elif len(argv) == 2:
	show_sales(int(argv[1]))
elif len(argv) == 3:
	show_sales(int(argv[1]), int(argv[2]))
