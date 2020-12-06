from django.core.exceptions import ValidationError
from django.test import TestCase

from utils.city.check_city import check_city


class CheckCityTest(TestCase):
    def test_return_None(self):
        city = "CAPITAO POCO"
        self.assertIsNone(check_city(city))

    def test_raise_error_if_city_not_valid(self):
        city = "Fake city"
        with self.assertRaises(ValidationError):
            check_city(city)
