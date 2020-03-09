import unittest
from Homework_5.task_3.src.is_triangle import is_triangle


class TriangleExistsTests(unittest.TestCase):

    def test_triangle_exists(self):
        self.assertEqual(is_triangle(2, 2, 2), True)

    def test_triangles_not_exists(self):
        self.assertEqual(is_triangle(1, 2, 3), False)

    def test_enter_integers_as_string(self):
        self.assertEqual(is_triangle('3', '2', '2'), True)

    def test_enter_floats_as_string(self):
        self.assertEqual(is_triangle(5.99, 4.01, 2.00), True)

    def test_enter_negative_numbers(self):
        self.assertEqual(is_triangle(-2, -2, -2), False)

    def test_enter_all_0(self):
        self.assertEqual(is_triangle(0, 0, 0), False)

    def test_enter_a_0(self):
        self.assertEqual(is_triangle(0, 1, 2), False)

    def test_enter_b_0(self):
        self.assertEqual(is_triangle(1, 0, 2), False)

    def test_enter_c_0(self):
        self.assertEqual(is_triangle(1, 1, 0), False)

    def test_enter_letters(self):
        self.assertEqual(is_triangle('a', 2, 2), f'Error. Only positive integers are available.')

    def test_enter_special_characters(self):
        self.assertEqual(is_triangle(2, "*", 2), f'Error. Only positive integers are available.')

    def test_enter_no_arguments(self):
        self.assertRaises(TypeError, lambda: is_triangle())

    def test_enter_less_arguments(self):
        self.assertRaises(TypeError, lambda: is_triangle(2, 2))

    def test_enter_extra_arguments(self):
        self.assertRaises(TypeError, lambda: is_triangle(2, 2, 2, 2))


if __name__ == "__main__":
    unittest.main()


