def is_triangle(a, b, c):
    try:
        if (int(a) + int(b) > int(c)) and (int(b) + int(c) > int(a)) and (int(a) + int(c) > int(b)):
            return True
        else:
            return False
    except ValueError:
        return f'Error. Only positive integers are available.'

# print(is_triangle())