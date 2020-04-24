
from lesson7 import Cell

first_cell = Cell(15)
second_cell = Cell(5)
third_cell = first_cell/second_cell
print(f"Деление - ", third_cell)
print(third_cell.make_order(2))
third_cell = first_cell+second_cell
print(f"Сложение - ", third_cell)
print(third_cell.make_order(5))

third_cell = first_cell*second_cell
print(f"Умножение - ", third_cell)
print(third_cell.make_order(15))

third_cell = first_cell-second_cell
print(f"Вычитание - ", third_cell)
print(third_cell.make_order(4))

