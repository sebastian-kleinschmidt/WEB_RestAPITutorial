from django.test import TestCase

from app.calc import add, subtract


def CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that two numbers are added together """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Test that two numbers are substracted correctly """
        self.assertEqual(subtract(5, 7), -2)
