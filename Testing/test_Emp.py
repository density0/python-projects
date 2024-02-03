import unittest
from Emp import Employee


class test_Emp(unittest.TestCase):

    def setUp(self):
        self.matt = Employee("matt", "king", 0)

    def test_give_default_raise(self):
        self.matt.give_raise()
        self.assertEqual(self.matt.get_salary(), '5000')

    def test_give_custom_raise(self):
        self.matt.give_raise(500)
        self.assertEqual(self.matt.get_salary(), '500')


    if __name__ == '__main__':
        unittest.main()
