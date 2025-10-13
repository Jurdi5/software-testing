# -*- coding: utf-8 -*-
"""
Source code for mock up testing examples.
"""
import subprocess
import time
import requests


def fetch_data_from_api(url):
    """Fetches data from an external API using the requests library."""
    response = requests.get(url, timeout=10)
    return response.json()


def read_data_from_file(filename):
    """Read data from a file."""
    try:
        with open(filename, encoding="utf-8") as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        raise e


def execute_command(command):
    """Execute a command in a subprocess."""
    try:
        result = subprocess.run(command, capture_output=True, check=False, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise e


def perform_action_based_on_time():
    """Perform an action based on the current time."""
    current_time = time.time()
    if current_time < 10:
        return "Action A"
    return "Action B"


# =============================================================================
# TESTS
# =============================================================================

import unittest
from unittest.mock import patch, mock_open


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """
    @patch("__main__.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        # Set up the mock response
        mock_get.return_value.json.return_value = {"key": "value"}
        
        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/data")
        
        # Assert that the function returns the expected result
        self.assertEqual(result, {"key": "value"})
        
        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class.
    """
    @patch("builtins.open", new_callable=mock_open, read_data="Hello from file")
    def test_read_data_from_file_success(self, mock_file):
        """
        Success case - file exists and is read correctly.
        """
        # Call the function under test
        result = read_data_from_file("test.txt")
        
        # Assert that the function returns the expected result
        self.assertEqual(result, "Hello from file")
        
        # Assert that open was called with the correct filename
        mock_file.assert_called_once_with("test.txt", encoding="utf-8")
    
    @patch("builtins.open", side_effect=FileNotFoundError("File not found"))
    def test_read_data_from_file_not_found(self, mock_file):
        """
        Error case - file does not exist.
        """
        # Assert that FileNotFoundError is raised
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("nonexistent.txt")
        
        # Assert that open was called
        mock_file.assert_called_once_with("nonexistent.txt", encoding="utf-8")


class TestExecuteCommand(unittest.TestCase):
    """
    Execute command unittest class.
    """
    @patch("__main__.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Success case - command executes successfully.
        """
        # Set up the mock response
        mock_run.return_value.stdout = "Command output"
        
        # Call the function under test
        result = execute_command(["echo", "Hello"])
        
        # Assert that the function returns the expected result
        self.assertEqual(result, "Command output")
        
        # Assert that subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with(
            ["echo", "Hello"],
            capture_output=True,
            check=False,
            text=True
        )


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform action based on time unittest class.
    """
    @patch("__main__.time.time")
    def test_perform_action_before_threshold(self, mock_time):
        """
        Test when current time is less than 10.
        """
        # Set up the mock to return a time less than 10
        mock_time.return_value = 5.0
        
        # Call the function under test
        result = perform_action_based_on_time()
        
        # Assert that the function returns "Action A"
        self.assertEqual(result, "Action A")
        
        # Assert that time.time was called
        mock_time.assert_called_once()
    
    @patch("__main__.time.time")
    def test_perform_action_after_threshold(self, mock_time):
        """
        Test when current time is greater than or equal to 10.
        """
        # Set up the mock to return a time greater than or equal to 10
        mock_time.return_value = 15.0
        
        # Call the function under test
        result = perform_action_based_on_time()
        
        # Assert that the function returns "Action B"
        self.assertEqual(result, "Action B")
        
        # Assert that time.time was called
        mock_time.assert_called_once()


if __name__ == "__main__":
    unittest.main()