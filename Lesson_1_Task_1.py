duration = int(input("Укажите суммарное количество секунд: "))

days = duration // 86400
hours = (duration % 86400) // 3600
minutes = (duration % 3600) // 60
seconds = duration % 60

print(days, "дней", hours, "часов", minutes, "минут", seconds, "секунд")