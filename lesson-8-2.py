from lesson8 import Division

first = [100, 0, 123, 34, 34, 2, 2, 345, -34]
second = [20, 10, 0, 'sdf', [1, 3], False, {'key': '123'}, None, 23]
print('****************************** Start program **********************************')
count = 0
while count < len(first):
    my_div = Division(first[count], second[count])
    print(f"{count}: {first[count]} / {second[count]} = ", my_div.processing())
    count += 1
print('******************************** End program **********************************')