from lesson8 import Complex

first_complex = Complex(7, -4)
second_complex = Complex(3, 2)
print('****************************** Start program **********************************')
add = (first_complex + second_complex)
print(f"Результат сложения комплексных чисел: ({first_complex}) + ({second_complex}) = ", add)
sub = (first_complex - second_complex)
print(f"Результат вычитания комплексных чисел: ({first_complex}) - ({second_complex}) = ", sub)
mul = (first_complex * second_complex)
print(f"Результат умножения комплексных чисел: ({first_complex}) * ({second_complex}) = ", mul)
div = (first_complex / second_complex)
print(f"Результат деления комплексных чисел: ({first_complex}) / ({second_complex}) = ", div)
print('******************************** End program **********************************')
