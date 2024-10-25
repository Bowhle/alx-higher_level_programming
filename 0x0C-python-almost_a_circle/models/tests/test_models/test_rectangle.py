# tests/test_models/test_rectangle.py
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_area(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)

    def test_display(self):
        """Test the display method."""
        r2 = Rectangle(3, 2)

        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        r2.display()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        expected_output = '###\n###\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            Rectangle('width', 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 'height')
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 'x')
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -1)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 0, 'y')
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -1)


if __name__ == "__main__":
    unittest.main()
