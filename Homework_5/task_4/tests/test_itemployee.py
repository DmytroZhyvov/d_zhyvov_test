import unittest
from Homework_5.task_1_3 import ITEmployee


class ITEmployeeTests(unittest.TestCase):

    def setUp(self):
        self.itemployee = ITEmployee('Alex Ivanov', 1990, 'QA', 2, 1000)

    def tearDown(self):
        self.itemployee = ITEmployee('Alex Ivanov', 1990, 'QA', 2, 1000)

    def test_full_name(self):
        self.assertEqual(self.itemployee.full_name, 'Alex Ivanov')

    def test_first_name(self):
        self.assertEqual(self.itemployee.get_name(), 'Alex')

    def test_last_name(self):
        self.assertEqual(self.itemployee.get_surname(), 'Ivanov')

    def test_birth_year(self):
        self.assertEqual(self.itemployee.birth_year, 1990)

    def test_position(self):
        self.assertEqual(self.itemployee.position, 'QA')

    def test_experience(self):
        self.assertEqual(self.itemployee.experience, 2)

    def test_salary(self):
        self.assertEqual(self.itemployee.salary, 1000)

    def test_change_salary(self):
        self.assertEqual(self.itemployee.salary, 1000)
        self.assertEqual(self.itemployee.raise_salary(500), 1500)

    def test_skill(self):
        self.assertEqual(self.itemployee.skills, [])

    def test_add_single_skill(self):
        self.assertEqual(self.itemployee.add_skills('API testing'), ['API testing'])

    def test_add_multiple_skills(self):
        self.assertEqual(self.itemployee.add_skills('GUI testing', 'Stress testing'), ['GUI testing', 'Stress testing'])



if __name__ == "__main__":
    unittest.main()