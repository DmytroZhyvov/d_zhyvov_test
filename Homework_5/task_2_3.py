# Task 2_3

import datetime


class Student:
    """Student class"""

    def __init__(self, full_name, speciality, year_of_enrolment, grades=[]):
        """"Constructor"""

        self.full_name = full_name
        self.speciality = speciality
        self.year_of_enrolment = year_of_enrolment
        self.grades = grades

    def __str__(self):
        """String representation of class"""
        return f'Student: full name - {self.full_name}, speciality - {self.speciality}, ' \
               f'year of enrolment - {self.year_of_enrolment}'

    def add_grades(self, *grade):
        """Adds grades to a Student grade list"""
        for x in grade:
            self.grades.append(x)
        return self.grades

    def get_mean_grade(self):
        """Calculates a mean grade"""
        try:  # added if a Student has no grades
            mean_grade = sum(self.grades) / len(self.grades)
            return mean_grade
        except ZeroDivisionError:
            return f'Grades list is empty. Please, add grades.'

    def get_duration_of_studying(self):
        """Calculates duration of studying in years"""
        current_year = datetime.date.today().year
        duration = current_year - self.year_of_enrolment
        return duration

