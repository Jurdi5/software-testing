import unittest

class TestPasswordValidator(unittest.TestCase):
    def test_valid_password(self):
        result = validate_password("Abcde12!")
        self.assertTrue(result.is_valid)
        self.assertEqual(result.errors, "")

    def test_short_password(self):
        result = validate_password("Ab1!")
        self.assertFalse(result.is_valid)
        self.assertIn("Password must be at least 8 characters", result.errors)

    def test_missing_numbers(self):
        result = validate_password("Abcdefgh!")
        self.assertFalse(result.is_valid)
        self.assertIn("The password must contain at least 2 numbers", result.errors)

    def test_missing_capital(self):
        result = validate_password("abcdef12!")
        self.assertFalse(result.is_valid)
        self.assertIn("password must contain at least one capital letter", result.errors)

    def test_missing_special_char(self):
        result = validate_password("Abcdef12")
        self.assertFalse(result.is_valid)
        self.assertIn("password must contain at least one special character", result.errors)

    def test_multiple_errors(self):
        result = validate_password("somepassword")
        self.assertFalse(result.is_valid)
        self.assertIn("Password must be at least 8 characters", result.errors)
        self.assertIn("The password must contain at least 2 numbers", result.errors)
        self.assertIn("password must contain at least one capital letter", result.errors)
        self.assertIn("password must contain at least one special character", result.errors)