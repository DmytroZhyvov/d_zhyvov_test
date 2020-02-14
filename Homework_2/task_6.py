# Определить совпадают ли числа.

a = int(input("Please, enter your number: "))
b = int(input("Please, enter your number: "))
c = int(input("Please, enter your number: "))

if a == b == c:
    print(3)
elif a == b:
    print(2)
elif a == c:
    print(2)
elif c == b:
    print(2)
else:
    print(0)

