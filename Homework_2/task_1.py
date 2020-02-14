# 1.
# Определить является ли строка записью числа.

string_1 = input('Please, enter any value: ')
print(string_1.isnumeric())


# 2.
# Посчитать сколько пробелов в строке.

string_2 = input('Please, enter any values with Spaces: ')
print(string_2.count(' '))


# 3.
# Посчитать сколько символов точки "." в строке.

string_3 = input('Please, enter any values with dots: ')
print(string_3.count('.'))


# 4.
# Создать строку "Homework". Преобразовать в строку длиной 100 символов. Посередине - исходное слово, по бокам
# пробелы.

string_4 = input('Please, enter "Homework": ')
print(string_4.center(100, " "))


# 5.
# Сделать первые буквы слов строки большими.

string_5 = input('Please, enter multiple values: ')
print(string_5.title())

