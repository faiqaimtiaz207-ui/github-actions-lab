import unittest
from app import add_numbers, multiply_numbers


class TestApp(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_multiplication(self):
        self.assertEqual(multiply_numbers(2, 3), 6)


if __name__ == "__main__":
    unittest.main()