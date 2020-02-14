# 1.
# Вычислить длину гипотенузы в прямоугольном треугольнике со сторонами 158 и 971.

side_1 = 158
side_2 = 971
hypotenuse = (side_1**2 + side_2**2)**0.5
print(hypotenuse)


# 2.
# Дано двузначное число. Найти число десятков в нем.

number_2 = int(input('Please, enter your number from 10 to 99: '))
result = number_2 // 10
print(result)


# 3.
# Дано трехзначное число. Посчитать сумму его цифр.

number_3 = input('Please, enter your number from 100 to 999: ')
first_num = number_3[0]
second_num = number_3[1]
third_num = number_3[2]
summa = int(first_num)+int(second_num)+int(third_num)
print(summa)


# 4.
# Дано целое число n. Выведете следующее за ним четное число.

n = int(input('Please, enter your number: '))
if n % 2 != 0:
    print(n+1)
else:
    print(n+2)

# 5.
# Дано положительное действительное число Х. Вывести его дробную часть.
X = input('Please, enter your broken number: ')
my_list = X.split('.')
result = str(my_list[1])
result = int(result)
print(result)

# 6.
# Дано положительное действительное число Х. Вывести первую цифру после десятичной точки.
X = input('Please, enter your broken number: ')
my_list = X.split('.')
result = str(my_list[1])[0:1]
result = int(result)
print(result)

