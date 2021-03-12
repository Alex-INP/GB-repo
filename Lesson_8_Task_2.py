import re

check = re.compile(
	r'^(?:\d+\.){3}\d|\d{2}[/]\w+[/](?:\d+[:]){3}\d+\s[+]\d+|\b\w+(?=\s[/])|(?:[/]\w+)+(?=\s)|\d+(?=\s\d+)|\d+(?=\s["])')

with open("nginx_logs.txt", encoding="utf-8") as f:
	for line in f:
		print(re.findall(check, line))
