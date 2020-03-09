# Task 1_3

from Homework_5.task_1_2 import Employee


class ITEmployee(Employee):
    """Employee with skills"""

    def __init__(self, full_name, birth_year, position, experience, salary):
        """Constructor"""

        super().__init__(full_name, birth_year, position, experience, salary)

        self.skills = []

    def __str__(self):
        """String representation of a class"""
        return f'Employee object: full name - {self.full_name}, birth year - {self.birth_year}, ' \
               f'position - {self.position}, experience - {self.experience}, salary - {self.salary}, ' \
               f'skill - {self.skills}'

    def add_skills(self, *new_skills):
        """Adds skills to Employee"""

        for skill in new_skills:
            self.skills.append(skill)
        return self.skills
