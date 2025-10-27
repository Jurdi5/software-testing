import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_regular_number(self):
        self.assertEqual(fizz_buzz(1), "1")

    def test_fizz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizz_buzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        