import unittest

from format_price import format_price

# -*- coding: utf-8 -*-
class TestFormatPrice(unittest.TestCase):
    def test_integer_values(self):
        price = format_price(4245)
        self.assertEqual(price, '4 245')

    def test_float_values(self):
        price = format_price(3245.42342)
        self.assertIsNotNone(price, '3 245.42')

    def test_negative_price(self):
        price = format_price(-56.01)
        self.assertEqual(price, None)

    def test_integer_with_nulls(self):
        price = format_price('446,000000')
        self.assertEqual(price, '446')

    def test_incorrect_type_values(self):
        price_one = format_price([587.6])
        price_two = format_price((123213, 3213))
        price_three = format_price({'abc'})
        self.assertEqual((price_one, price_two, price_three), (None, None, None))

if __name__ == '__main__':
    unittest.main()