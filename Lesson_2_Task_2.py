original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for i in original_list:
	if i[0] == "-" or i[0] == "+":
		if i[1:].isdigit():
			new_list.extend(["'", f"{i[0]}{int(i):02}", "'"])
	elif i.isdigit():
		new_list.extend(["'", f"{int(i):02}", "'"])
	else:
		new_list.append(i)
print(" ".join(new_list))
