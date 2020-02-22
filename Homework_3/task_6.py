# Task 6

# 6.1
# Ask user to enter a correct number.
def number_checking():

    while True:
        value = input('Please, enter a number: ')
        try:
            float(value)
            return print('Thank you!')
        except ValueError:
            pass
            print('Try again!')

number_checking()


# 6.2
# Ask user to enter a correct word.

# Variant 1
def word_checking():

    while True:
        value = input('Please, enter a word: ')
        value = value.strip(' ')
        if ' ' not in value and value.isalpha():
            return print('Thank you!')
        else:
            print('Try again!')

word_checking()

# Variant 2
def word_checking():

    while True:
        value = input('Please, enter a word: ')
        value = value.strip(' ')
        value = value.split(' ')
        if len(value) != 1:
            print('Try again!')
        else:
            for x in value:
                if x.isalpha():
                    return print('Thank you!')
                else:
                    print('Try again!')

word_checking()

# 6.3
# Check a leap year.

def is_leap_year(year):
    year = int(year)
    if year % 4 == 0:
        return print(True)
    elif year % 100 != 0:
        if year % 400 == 0:
            return print(True)
        else:
            return print(False)

is_leap_year(2020)


# 6.4
# Check if triangle is valid.
def is_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False

is_triangle(2,2,2)


# 6.5
# Check triangle type.

def triangle_type(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        if a == b == c:
            return print('Equilateral triangle')
        elif (a == b) or (a == c) or (b == c):
            return print('Isosceles triangle')
        else:
            return print('Versatile triangle')
    else:
        return print('Not a triangle')

triangle_type(4,2,2)

# 6.6
# Check distance between points.

def distance(x1, y1, x2, y2):
    result = ((x2-x1)**2 + (y2 - y1)**2) ** 0.5
    return print(result)

distance(1,2,2,3)