# test_main.py
import unittest
from main import greet, farewell  # импортируйте обе функции

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

class TestFarewellFunction(unittest.TestCase):
    def test_farewell(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")

if __name__ == "__main__":
    unittest.main()