import unittest
from Homework_5.task_3.src.is_leap_year import is_leap_year


class LeapYearTests(unittest.TestCase):
    def test_enter_leap_year(self):
        self.assertEqual(is_leap_year(2020), True)

    def test_enter_common_year(self):
        self.assertFalse(is_leap_year(2021))

    def test_enter_zero(self):
        self.assertTrue(is_leap_year(0))

    def test_enter_negative_digit(self):
        self.assertEqual(is_leap_year(-1), f'Year must be a positive integer.')

    def test_no_argument(self):
        self.assertRaises(TypeError, lambda: is_leap_year())

    def test_enter_letters(self):
        self.assertEqual(is_leap_year('Abcd'), f'Year must be a positive integer.')

    def test_enter_symbols(self):
        self.assertEqual(is_leap_year('!@#^&'), f'Year must be a positive integer.')


if __name__ == "__main__":
    unittest.main()


