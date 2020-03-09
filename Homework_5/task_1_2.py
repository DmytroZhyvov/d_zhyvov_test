# Task_1_2

from Homework_5.task_1_1 import Person


class Employee(Person):
    """"Employee class"""

    def __init__(self, full_name, birth_year, position, experience, salary):
        """Constructor"""
        super().__init__(full_name, birth_year)
        """Inheritance from Person class"""

        self.position = position  # set an Employee position

        self.experience = experience  # set an Employee experience
        try:
            if not experience >= 0:  # check that experience is int and >= 0
                raise ValueError('Experience can not be lower, than 0!')
        except TypeError:
            print('Experience is not correct!')
            self.experience = None

        self.salary = salary  # set an Employee salary
        try:
            if not salary >= 0:  # check that salary is int and >= 0
                raise ValueError('Salary can not be lower, than 0!')
        except TypeError:
            print('Salary is not correct!')
            self.salary = None

    def __str__(self):
        """String representation of a class"""
        return f'Employee object: full name - {self.full_name}, birth year - {self.birth_year}, ' \
               f'position - {self.position}, experience - {self.experience}, salary - {self.salary}'

    def return_qualification_w_position(self):
        """Returns qualification depending on experience"""

        if self.experience < 3:
            qualification = f'Junior {self.position}'
        elif 3 <= self.experience < 6:
            qualification = f'Middle {self.position}'
        else:
            qualification = f'Senior {self.position}'
        return qualification

    def raise_salary(self, amount):
        """Increase salary"""

        self.salary = self.salary + amount
        return self.salary



