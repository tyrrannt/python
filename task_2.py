"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""


def merge(left_list, right_list):
    result = []
    left_index = 0
    right_index = 0
    left_len = len(left_list)
    right_len = len(right_list)
    for _ in range(left_len + right_len):
        if left_index < left_len and right_index < right_len:
            if left_list[left_index] <= right_list[right_index]:
                result.append(left_list[left_index])
                left_index += 1
            else:
                result.append(right_list[right_index])
                right_index += 1
        elif left_index == left_len:
            result.append(right_list[right_index])
            right_index += 1
        elif right_index == right_len:
            result.append(left_list[left_index])
            left_index += 1
    return result


def merge_sort(lst_obj):
    if len(lst_obj) <= 1:
        return lst_obj
    middle = len(lst_obj) // 2
    left_list, right_list = merge_sort(lst_obj[:middle]), merge_sort(lst_obj[middle:])
    return merge(left_list, right_list)


if __name__== '__main__':
    lst_obj = [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
    print(f'Исходный: {lst_obj}')
    sort_lst_obj = merge_sort(lst_obj)
    print(f'Отсортированный: {sort_lst_obj}')
