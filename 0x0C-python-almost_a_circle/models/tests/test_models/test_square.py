# tests/test_models/test_square.py
import unittest
from io import StringIO
import sys
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_str_method(self):
        s1 = Square(5, 2, 3, 10)
        self.assertEqual(str(s1), "[Square] (10) 2/3 - 5")

    def test_area(self):
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_area_different_size(self):
        s2 = Square(7)
        self.assertEqual(s2.area(), 49)

    def test_display(self):
        """Test the display method."""
        s3 = Square(3, 1, 1)

        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        s3.display()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        expected_output = "\n" + " " * 1 + "###\n" + " " * 1 + "###\n" + " " * 1 + "###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_custom_id(self):
        s4 = Square(4, 1, 1, 99)
        self.assertEqual(s4.id, 99)

    def test_default_id(self):
        s5 = Square(4)
        self.assertIsNotNone(s5.id)

    def test_size_validation(self):
        with self.assertRaises(TypeError):
            Square("4")
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            Square(2, "1")
        with self.assertRaises(ValueError):
            Square(2, -1)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            Square(2, 0, "1")
        with self.assertRaises(ValueError):
            Square(2, 0, -1)

    def test_large_values(self):
        s6 = Square(1000000)
        self.assertEqual(s6.area(), 1000000000000)

if __name__ == "__main__":
    unittest.main()
