"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from random import randint

@profile
def search_in_list(search_el):
    lst2 = [randint(0, i) for i in range(100000)]
    result = []
    result2 = []
    for i in lst2:
        if i == search_el:
            result.append(i)
    lst1 = len(result) * lst2
    for j in lst1:
        if i == search_el:
            result2.append(i)
    del lst2
    return len(result), len(result2)


print(search_in_list(25))

