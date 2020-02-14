# Вывести числа в порядке возрастания.

a = input("Please enter your number: ")
b = input("Please enter your number: ")
c = input("Please enter your number: ")

if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= b <= a:
    print(c, b, a)
elif c <= a <= b:
    print(c, a, b)