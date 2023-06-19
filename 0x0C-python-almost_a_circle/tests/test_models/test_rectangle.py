#!/usr/bin/python3
"""
Unittest for Rectangle Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r = Rectangle(2, 3, 1, 1, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 1)

    def test_width(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)
        r.width = 5
        self.assertEqual(r.width, 5)
        with self.assertRaises(TypeError):
            r.width = "5"
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.height, 3)
        r.height = 5
        self.assertEqual(r.height, 5)
        with self.assertRaises(TypeError):
            r.height = "5"
        with self.assertRaises(ValueError):
            r.height = -5

    def test_x(self):
        r = Rectangle(2, 3, 1, 1)
        self.assertEqual(r.x, 1)
        r.x = 5
        self.assertEqual(r.x, 5)
        with self.assertRaises(TypeError):
            r.x = "5"
        with self.assertRaises(ValueError):
            r.x = -5

    def test_y(self):
        r = Rectangle(2, 3, 1, 1)
        self.assertEqual(r.y, 1)
        r.y = 5
        self.assertEqual(r.y, 5)
        with self.assertRaises(TypeError):
            r.y = "5"
        with self.assertRaises(ValueError):
            r.y = -5

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        r = Rectangle(2, 3)
        expected_output = "##\n" \
                          "##\n" \
                          "##\n"
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(2, 3, 1, 1, 1)
        expected_output = "Rectangle (1) 1/1 2/3"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        r = Rectangle(2, 3, 1, 1, 1)
        r.update(2, 4, 5, 2, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

        r.update(width=6, height=7, x=3, y=3)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 3)

    def test_to_dictionary(self):
        r = Rectangle(2, 3, 1, 1, 1)
        expected_output = {'id': 1, 'width': 2, 'height': 3, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), expected_output)


if __name__ == "__main__":
    unittest.main()

