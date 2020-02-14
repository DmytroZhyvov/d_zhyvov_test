# Определить существование треугольника.

a = 2
b = 2
c = 2

if a+b > c:
    if a+c > b:
        if b+c > a:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")

