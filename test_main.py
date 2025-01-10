# test_main.py
import unittest
from main import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()

class TestFarewell(unittest.TestCase):
    def test_farewell(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")