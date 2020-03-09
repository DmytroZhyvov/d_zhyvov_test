def is_leap_year(year):
    try:
        year = int(year)

        if year < 0:
            raise ValueError

        if year % 4 == 0:
            return True
        elif year % 100 != 0:
            if year % 400 == 0:
                return True
            else:
                return False

    except ValueError:
        return f'Year must be a positive integer.'


