# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(my_str, variable=1):
    if variable != 1:
        return my_str.capitalize()
    else:
        result = my_str[0].upper() + my_str[1:].lower()
        return result

def int_long_func(my_str, variable=1):
    result = []
    if variable != 1:
        return my_str.capitalize()
    else:
        middle = my_str.split(' ')
        print(middle)
        for arg in middle:
            result.append(arg[0].upper() + arg[1:].lower())
        return str(result)
print(int_func('прОСвет'))
print(int_long_func('соотношение экрана к поверхности', 0))
