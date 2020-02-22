# Task 3

# 3.1
i = 0

while i <= 10:
    print(i)
    i += 1



# 3.2
i = 20

while i >= 0:
    print(i, end=' ')
    i -= 1



# 3.3

value = int(input('Please, enter a value: '))
n = 0
while True:
    if value % 2 == 0:
        value /= 2
        n += 1
    else:
        print(n)
        break

