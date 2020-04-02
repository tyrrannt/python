# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введите сумму выручки: "))
cost = int(input("Введите сумму издержек: "))
fin_result = revenue - cost
if fin_result <= 0:
    print("У фирмы отсутствует прибыль.")
else:
    profitability = fin_result / revenue
    print(f"Прибыль фирмы составила {fin_result}, а рентабельность выручки составляет {profitability:.2f}")
    number_staff = int(input("Введите численность сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет {(fin_result / number_staff):.2f}")