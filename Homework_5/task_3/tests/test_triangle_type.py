import unittest
from Homework_5.task_3.src.triangle_type import triangle_type

class TriangleTypeTests(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(triangle_type(2, 2, 2), f'Equilateral triangle')

    def test_isosceles_triangle_a_equal_b(self):
        self.assertEqual(triangle_type(3, 3, 2), f'Isosceles triangle')

    def test_isosceles_triangle_a_equal_c(self):
        self.assertEqual(triangle_type(3, 2, 3), f'Isosceles triangle')

    def test_isosceles_triangle_b_equal_c(self):
        self.assertEqual(triangle_type(2, 3, 3), f'Isosceles triangle')

    def test_versatile_triangle(self):
        self.assertEqual(triangle_type(2, 4, 5), f'Versatile triangle')

    def test_not_a_triangle(self):
        self.assertEqual(triangle_type(1, 2, 3), f'Not a triangle')

    def test_enter_integers_as_string(self):
        self.assertEqual(triangle_type('3', '2', '2'), f'Isosceles triangle')

    def test_enter_floats_as_string(self):
        self.assertEqual(triangle_type(5.99, 4.01, 2.00), f'Versatile triangle')

    def test_enter_negative_numbers(self):
        self.assertEqual(triangle_type(-2, -2, -2), f'Not a triangle')

    def test_enter_all_0(self):
        self.assertEqual(triangle_type(0, 0, 0), f'Not a triangle')

    def test_enter_a_0(self):
        self.assertEqual(triangle_type(0, 1, 2), f'Not a triangle')

    def test_enter_b_0(self):
        self.assertEqual(triangle_type(1, 0, 2), f'Not a triangle')

    def test_enter_c_0(self):
        self.assertEqual(triangle_type(1, 1, 0), f'Not a triangle')

    def test_enter_letters(self):
        self.assertEqual(triangle_type('a', 2, 2), f'Error. Only positive integers are available.')

    def test_enter_special_characters(self):
        self.assertEqual(triangle_type(2, "*", 2), f'Error. Only positive integers are available.')

    def test_enter_no_arguments(self):
        self.assertRaises(TypeError, lambda: triangle_type())

    def test_enter_less_arguments(self):
        self.assertRaises(TypeError, lambda: triangle_type(2, 2))

    def test_enter_extra_arguments(self):
        self.assertRaises(TypeError, lambda: triangle_type(2, 2, 2, 2))


if __name__ == "__main__":
    unittest.main()


