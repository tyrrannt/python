# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
name = input("Введите свое имя:")
surname = input("Введите свою фамилию:")
height = int(input("Введите свой рост (см):"))
weight = int(input("Введите свой вес (кг):"))
bmi = weight / (height * height / 10000)
reformat_string = f"{surname} {name} при росте {height} и весе {weight} индекс массы тела = {bmi:.2f} - "
if bmi <= 16:
    print(reformat_string + "Выраженный дефицит массы тела")
elif 16 < bmi <= 18.5:
    print(reformat_string + "Недостаточная (дефицит) масса тела")
elif 18.5 < bmi <= 25:
    print(reformat_string + "Норма")
elif 25 < bmi <= 30:
    print(reformat_string + "Избыточная масса тела (предожирение)")
elif 30 < bmi <= 35:
    print(reformat_string + "Ожирение первой степени")
elif 35 < bmi <= 40:
    print(reformat_string + "Ожирение второй степени")
else:
    print(reformat_string + "Ожирение третьей степени (морбидное)")
