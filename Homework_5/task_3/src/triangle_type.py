def triangle_type(a, b, c):
    """Check whether a triangle exists and returns its type"""

    try:
        a = int(a)  # triangle side
        b = int(b)  # triangle side
        c = int(c)  # triangle side

        if (a + b > c) and (b + c > a) and (a + c > b):
            if a == b == c:
                return f'Equilateral triangle'
            elif (a == b) or (a == c) or (b == c):
                return f'Isosceles triangle'
            else:
                return f'Versatile triangle'
        else:
            return f'Not a triangle'
    except ValueError:
        return f'Error. Only positive integers are available.'

