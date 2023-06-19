#!/usr/bin/python3
"""
Unittest for Square Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_square.py
"""


import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        s = Square(5, 1, 1, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 1)

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        with self.assertRaises(TypeError):
            s.size = "10"
        with self.assertRaises(ValueError):
            s.size = -10

    def test_str(self):
        s = Square(5, 1, 1, 1)
        expected_output = "Square (1) 1/1 - 5"
        self.assertEqual(str(s), expected_output)

    def test_update(self):
        s = Square(5, 1, 1, 1)
        s.update(2, 10, 2, 2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)

        s.update(size=15, x=3, y=3)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        s = Square(5, 1, 1, 1)
        expected_output = {'id': 1, 'size': 5, 'x': 1, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_output)

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()

