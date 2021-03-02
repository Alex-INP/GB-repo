from sys import argv

with open("bakery.csv","a", encoding="utf-8") as f:
	f.write(f"{argv[1]}\n")