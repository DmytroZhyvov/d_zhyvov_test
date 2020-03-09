# Task 2_1


class Room:
    """Room class"""

    def __init__(self, length, width):
        """Constructor"""
        self.length = length
        self.width = width

    def __str__(self):
        """String representation of class"""
        return f'Room class: length - {self.length}, width - {self.width}'

    def calculate_square(self):
        """Calculates square of Room"""
        square = self.length * self.width
        return square

    def calculate_perimeter(self):
        """"Calculates perimeter of Room"""
        perimeter = (self.length + self.width)*2
        return perimeter

