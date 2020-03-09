# Task 1_1

import datetime


class Person:
    """General info about a Person"""

    def __init__(self, full_name, birth_year):
        """Constructor"""

        self.full_name = full_name  # set a Person full name
        try:
            if self.full_name.replace(' ', '').isalpha() is not True:  # check, that full name consists of letters only
                raise ValueError("Full Name is not correct!")
            elif len(self.full_name.split()) != 2:  # check, that full name consists of two elements
                raise ValueError("Full Name is not correct!")
        except AttributeError:
            print("Full Name is not correct!")  # display error message
            self.full_name = None

        self.birth_year = birth_year  # set a Person year of birth
        try:
            if not 1900 <= self.birth_year <= 2019:  # check that year of birth is correct
                raise ValueError("Birth year is not correct!")
        except TypeError:
            print("Birth year is not correct!")
            self.birth_year = None

    def __str__(self):
        """String representation of a class"""
        return f'Person object: full name - {self.full_name}, birth year - {self.birth_year}.'

    def get_name(self):
        """Gets a Person's first name"""
        try:
            name = self.full_name.split()[0]
            return name
        except IndexError:
            print("Full Name is not correct!")

    def get_surname(self):
        """Gets a Person's last name"""
        try:
            surname = self.full_name.split()[1]
            return surname
        except IndexError:
            print("Full Name is not correct!")

    def get_age(self, *year):
        """Gets a Person's age in specified year. Current year is a default value."""

        current_year = datetime.date.today().year  # get a current year
        age = []

        if self.birth_year is None:
            raise ValueError('Birth year is not correct!')

        try:
            if len(year) >= 1:  # check that more than 1 parameter is given
                for x in year:
                    age.append(x - self.birth_year)
            else:
                age.append(current_year - self.birth_year)  # use default parameter
            return age

        except TypeError:
            print("Year is not correct!")

