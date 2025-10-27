import unittest

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_newline_separator(self):
        self.assertEqual(add("1,2\n3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;3"), 4)
        self.assertEqual(add("//|\n1|2|3"), 6)
        self.assertEqual(add("//sep\n2sep5"), 7)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2")
        self.assertIn("Negative number(s) not allowed: -2", str(context.exception))

    def test_multiple_errors(self):
        with self.assertRaises(ValueError) as context:
            add("//|\n1|2,-3")
        self.assertIn("Negative number(s) not allowed: -3", str(context.exception))

    def test_ignore_large_numbers(self):
        self.assertEqual(add("2,1001"), 2)
