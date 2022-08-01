'''Задача 1. 10 баллов'''

print('task 1:')
str1: str = input('Введите строку \n')
if len(str1) < 2:
    print("Ваша строка слишком короткая - ", str1)
else:
    new_str = str1[0]+str1[1]+str1[-2]+str1[-1]
    print(new_str)


'''Задача 2. 15 баллов'''

print('task 2:')
sentence = 'Hillel school'
value = dict().fromkeys(set(sentence))
for key in value.keys():
    value[key] = sentence.count(key)
print(key, value)


"""Задача 3. 15 баллов"""

print('task 3:')
products = ['bread', 'milk', 'kolbasa']
products.sort(key=len)
pr = products.pop()
pr_len = len(pr)
result = 'Самое длинное название продукта {} длинна {} символов'.format(pr,pr_len )
print(result)


"""Задача 4. 5 баллов баллов"""

print('task 4:')
name = input('print your name \n')
little_word = name.upper()
big_word = name.lower()
result2 = '{} {}'.format(little_word, big_word)
print(result2)


"""Задача 5. 15 баллов"""

print('task 5:')
words = input('print some colors \n')
words = words.split(', ')
words = set(words)
words_list = list(words)
print(*sorted(words_list), sep=", ")


"""Задача 6. 5 баллов"""

print('task 6:')
cortej = input('print some number \n')
cortej = cortej.split(", ")
cortej = list(cortej)
cortej.pop()
cortej = tuple(cortej)
print(cortej)


"""Задача 7. 10 баллов"""

print('task 7:')
my_list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
my_list1 = [list(n) for n in my_list]
print(my_list1)


"""Задача 8. 15 баллов"""

print('task 8:')
for i in tuple(range(-99, 99, 3)):
    if i % 3 == 0:
        print(f'это число: {i}, делится без остатка на 3')


"""Задача 9. 10 баллов"""

print('task 9:')
list1 = [1, 2, 3]
list2 = [1, 4, 6, 4]
for i in list1:
    for j in list2:
        if i == j:
            result3 = bool(i == j)
            print(result3)
        else:
            break
