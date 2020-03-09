# Task 2_2


class Points:

    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def __str__(self):
        """String representation of class"""
        return f'A point with X-coordinate: {self.x} and Y-coordinate: {self.y}'

    def get_distance_from_the_origin(self):
        """Calculates a distance between a point and the origin"""

        distance = (self.x**2 + self.y**2)**0.5
        return distance

    def get_distance_between_points(self, class_object):
        """Calculates a distance between two points"""

        x = class_object.x  # "x" parameter of a class object
        y = class_object.y  # "y" parameter of a class object

        distance = ((x - self.x)**2 + (y - self.y)**2)**0.5
        return distance


