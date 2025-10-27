import unittest
import os
import json
import hashlib
from unittest.mock import patch, mock_open, MagicMock
import sys

try: 
    from examenEje1 import (
        generate_salt,
        generate_password_hash,
        load_user_data,
        save_user_data,
        register,
        login,
        USER_DATA_FILE
    )
except ErrorImport:
    print("No se pudo acceder")
    sys.exit(1)

class TestGenerateSalt(unittest.TestCase):
    def test_lenght(self):
        salt = generate_salt()
        self.assertEqual(len(salt), 32)
    
    def TestHexaSalt(self):
        salt = generate_salt()
        try:
            int(salt, 16)
            is_hex = True
        except ErrorValue:
            is_hex = False
        self.assertTrue(is_hex)
    
    def TestSaltType(self):
        salt = generate_salt()
        self.assertIsInstance(salt, str)

class TestGeneratePassword(unittest.TestCase):

    def testHashLenght(self):
        password_hash = generate_password_hash("test_password", "test_salt")
        self.assertEqual(len(password_hash), 64)

    def test_hash_is_hex(self):
        password_hash = generate_password_hash("test", "salt")
        try:
            int(password_hash, 16)
            is_hex = True
        except ValueError:
            is_hex = False
        self.assertTrue(is_hex)
    
    def test_empty_password(self):
        password_hash = generate_password_hash("", "salt")
        self.assertEqual(len(password_hash), 64)
    
    def test_special_characters(self):
        password_hash = generate_password_hash("!@#$%^&*()", "salt")
        self.assertEqual(len(password_hash), 64)


class TestLoadUserData(unittest.TestCase):
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='{"user1": {"password_hash": "hash", "salt": "salt"}}')
    def test_load_existing_file(self, mock_file, mock_exists):
        mock_exists.return_value = True
        data = load_user_data()
        self.assertIn("user1", data)
        self.assertEqual(data["user1"]["password_hash"], "hash")
    
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_load_empty_file(self, mock_file, mock_exists):
        mock_exists.return_value = True
        data = load_user_data()
        self.assertEqual(data, {})

class TestSaveUserData(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_data(self, mock_json_dump, mock_file):
        """Verifica que guarde los datos correctamente"""
        test_data = {"user1": {"password_hash": "hash", "salt": "salt"}}
        save_user_data(test_data)
        mock_file.assert_called_once_with(USER_DATA_FILE, "w")
        mock_json_dump.assert_called_once()
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_empty_data(self, mock_json_dump, mock_file):
        """Verifica que guarde un diccionario vacío"""
        test_data = {}
        save_user_data(test_data)
        mock_json_dump.assert_called_once()

class TestRregister(unittest.TestCase):
    @patch('builtins.input', return_value='test_password')
    @patch('examenEje1.load_user_data')
    @patch('examenEje1.save_user_data')
    @patch('examenEje1.generate_salt', return_value='test_salt')
    @patch('builtins.print')
    def test_register_new_user(self, mock_print, mock_salt, mock_save, mock_load, mock_input):
        mock_load.return_value = {}
        register("new_user")
        mock_save.assert_called_once()
        saved_data = mock_save.call_args[0][0]
        self.assertIn("new_user", saved_data)
        mock_print.assert_called_with("User registered successfully.")
    
    @patch('examenEje1.load_user_data')
    @patch('builtins.print')
    def test_register_existing_user(self, mock_print, mock_load):
        mock_load.return_value = {"existing_user": {"password_hash": "hash", "salt": "salt"}}
        register("existing_user")
        mock_print.assert_called_with("User already exists. Please choose a different username.")
    
class TestLogin(unittest.TestCase):
    @patch('examenEje1.load_user_data')
    @patch('builtins.print')
    def test_login_nonexistent_user(self, mock_print, mock_load):
        mock_load.return_value = {}
        login("nonexistent_user", "password")
        mock_print.assert_called_with("User does not exist. Please register first.")
    
    @patch('examenEje1.load_user_data')
    @patch('examenEje1.generate_password_hash')
    @patch('builtins.print')
    def test_login_correct_password(self, mock_print, mock_hash, mock_load):
        test_hash = "correct_hash"
        mock_load.return_value = {
            "test_user": {
                "password_hash": test_hash,
                "salt": "test_salt"
            }
        }
        mock_hash.return_value = test_hash
        login("test_user", "correct_password")
        mock_print.assert_called_with("Login successful!")
    
    @patch('examenEje1.load_user_data')
    @patch('examenEje1.generate_password_hash')
    @patch('builtins.print')
    def test_login_incorrect_password(self, mock_print, mock_hash, mock_load):
        mock_load.return_value = {
            "test_user": {
                "password_hash": "correct_hash",
                "salt": "test_salt"
            }
        }
        mock_hash.return_value = "wrong_hash"
        login("test_user", "wrong_password")
        mock_print.assert_called_with("Invalid password. Please try again.")
    
if __name__ == "__main__":
    unittest.main(verbosity=2)