#!/usr/bin/python3
"""Unittests for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the functionality of the Rectangle class."""

    def test_initialization(self):
        """Test initialization of the Rectangle object."""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

    def test_initialization_with_id(self):
        """Test initialization with a custom id."""
        r2 = Rectangle(5, 15, 2, 3, 99)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 15)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 99)

    def test_invalid_width_type(self):
        """Test if TypeError is raised for non-integer width."""
        with self.assertRaises(TypeError):
            Rectangle("10", 5)

    def test_invalid_height_type(self):
        """Test if TypeError is raised for non-integer height."""
        with self.assertRaises(TypeError):
            Rectangle(10, "5")

    def test_invalid_x_type(self):
        """Test if TypeError is raised for non-integer x."""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "2")

    def test_invalid_y_type(self):
        """Test if TypeError is raised for non-integer y."""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 2, "3")

    def test_invalid_width_value(self):
        """Test if ValueError is raised for width <= 0."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_invalid_height_value(self):
        """Test if ValueError is raised for height <= 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, -5)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_invalid_x_value(self):
        """Test if ValueError is raised for x < 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -2)

    def test_invalid_y_value(self):
        """Test if ValueError is raised for y < 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 2, -3)

    def test_area(self):
        """Test area calculation for the rectangle."""
        r3 = Rectangle(3, 4)
        self.assertEqual(r3.area(), 12)


if __name__ == "__main__":
    unittest.main()
