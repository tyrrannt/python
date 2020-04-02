# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_second = int(input("Введите время в секундах:"))
hours = time_second // 3600
minutes = (time_second % 3600) // 60
seconds = (time_second % 3600) % 60
if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)
print(f"{hours}:{minutes}:{seconds}")
