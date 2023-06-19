#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        # Test with empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test with non-empty list
        list_dictionaries = [{"id": 1, "width": 2, "height": 3}]
        expected_result = '[{"id": 1, "width": 2, "height": 3}]'
        self.assertEqual(Base.to_json_string(list_dictionaries),
                         expected_result)

    def test_save_to_file(self):
        # Test with list of Rectangle instances
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        expected_result = '[{"id": 1, "width": 1, "height": 2},
                            {"id": 2, "width": 3, "height": 4}]'
        self.assertEqual(content, expected_result)

        # Test with list of Square instances
        s1 = Square(5)
        s2 = Square(6)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            content = file.read()
        expected_result = '[{"id": 1, "size": 5}, {"id": 2, "size": 6}]'
        self.assertEqual(content, expected_result)

    def test_from_json_string(self):
        # Test with empty string
        self.assertEqual(Base.from_json_string(""), [])

        # Test with valid JSON string
        json_string = '[{"id": 1, "width": 2, "height": 3}]'
        expected_result = [{"id": 1, "width": 2, "height": 3}]
        self.assertEqual(Base.from_json_string(json_string), expected_result)

    def test_create(self):
        # Test with Rectangle class
        rectangle_dict = {"id": 1, "width": 2, "height": 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(rectangle_instance, Rectangle)
        self.assertEqual(rectangle_instance.id, 1)
        self.assertEqual(rectangle_instance.width, 2)
        self.assertEqual(rectangle_instance.height, 3)

        # Test with Square class
        square_dict = {"id": 2, "size": 5}
        square_instance = Square.create(**square_dict)
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 5)

    def test_load_from_file(self):
        # Test with Rectangle class
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)

        # Test with Square class
        s1 = Square(5)
        s2 = Square(6)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertIsInstance(squares, list)
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)


if __name__ == "__main__":
    unittest.main()
