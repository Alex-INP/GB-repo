original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index_modifier = 0
for i in range(len(original_list)):
	value = original_list[i + index_modifier]
	if value[0] == "-" or value[0] == "+":
		if value[1:].isdigit():
			original_list.pop(i + index_modifier)
			to_add = ["'", f"{value[0]}{int(value):02}", "'"]
			counter = 0
			for nu in range(3):
				original_list.insert(i + index_modifier + counter, to_add[counter])
				counter += 1
		index_modifier += 2
	elif value.isdigit():
		original_list.pop(i + index_modifier)
		to_add = ["'", f"{int(value):02}", "'"]
		counter = 0
		for nu in range(3):
			original_list.insert(i + index_modifier + counter, to_add[counter])
			counter += 1
		index_modifier += 2

print(" ".join(original_list))
