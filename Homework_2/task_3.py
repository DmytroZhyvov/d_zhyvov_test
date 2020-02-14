# Определить високосный ли год.

year = input('To check, please enter YYYY: ')
year = int(year)

if year % 4 == 0:
    print("YES")
elif year % 100 != 0:
    if year % 400 == 0:
        print("YES")
    else:
        print("NO")
