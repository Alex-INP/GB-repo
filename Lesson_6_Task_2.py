# Задание 1

# parsed_content = []
# with open("nginx_logs.txt", "r", encoding="utf-8") as f:
# 	for line in f:
# 		parsed_content.append((line.split(" ")[0], line.split(" ")[5][1:], line.split(" ")[6]))


# Задание 2
# from time import perf_counter

parsed_content = []
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
	for line in f:
		parsed_content.append(line.split(" ")[0])

spammer_id = None
spam_counter = 0

# Самый медленный вариант. (34.0219512)-----------------------------------------------------
# start_time = perf_counter()
#
# for i in parsed_content:
# 	if parsed_content.count(i) > spam_counter:
# 		spam_counter = parsed_content.count(i)
# 		spammer_id = i
#
# end_time = perf_counter()
# print(end_time - start_time)


# Средняя скорость. (7.4080879)--------------------------------------------------------------

# start_time = perf_counter()
#
# max_count =len(set(parsed_content))
# for i in range(max_count):
# 	element = parsed_content[0]
# 	#print(spammer_id)
# 	if parsed_content.count(element) > spam_counter:
# 		spam_counter = parsed_content.count(element)
# 		spammer_id = element
# 	for _ in range(parsed_content.count(element)):
# 		parsed_content.remove(element)
#
# end_time = perf_counter()
# print(end_time - start_time)


# Самый быстрый вариент. (0.014825000000000005)-----------------------------------------------
# start_time = perf_counter()

id_2, counter_2 = None, 0

for i in sorted(parsed_content):
	if i == id_2:
		id_2 = i
		counter_2 += 1
	else:
		if counter_2 > spam_counter:
			spammer_id = id_2
			spam_counter = counter_2
		id_2, counter_2 = i, 1

# end_time = perf_counter()
# print(end_time - start_time)

print("Спаммер: ", spammer_id, "\n", "Количество: ", spam_counter, sep="")
