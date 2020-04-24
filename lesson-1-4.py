# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input("Введите целое положительное число: "))
divider = 10
count = number % 10
while True:
    if (number // divider) > 0:
        mid_res = (number % (divider * 10)) // divider
        if count < mid_res:
            count = mid_res
    else:
        break
    divider *= 10
print(f"Наибольшая цифра в числе = {count}")
