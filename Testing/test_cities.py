import unittest
from city_function import city_country


class TestingCities(unittest.TestCase):
    """ Tests for 'city_function.py' """

    def test_city_function(self):
        location = city_country('New York', 'USA')
        self.assertEqual(location, 'New York, USA')

    def test_city_pop(self):
        location = city_country('NY', 'USA', '93823')
        self.assertEqual(location, "NY, USA - population 93823")

    if __name__ == '__main__':
        unittest.main()


TestingCities()
