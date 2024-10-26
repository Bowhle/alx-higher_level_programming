# tests/test_models/test_rectangle.py
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_str_method(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_area(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)

    def test_area_different_values(self):
        r5 = Rectangle(3, 7)
        self.assertEqual(r5.area(), 21)

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

    def test_custom_id(self):
        r3 = Rectangle(4, 5, 1, 1, 99)
        self.assertEqual(r3.id, 99)

    def test_default_id(self):
        r4 = Rectangle(4, 5)
        self.assertIsNotNone(r4.id)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("4", 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(2, "6")
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, "1")
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -1)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 0, "1")
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -1)

    def test_large_values(self):
        r7 = Rectangle(1000000, 1000000)
        self.assertEqual(r7.area(), 1000000000000)

    def test_update_method(self):
        r8 = Rectangle(4, 5, 1, 1, 20)
        r8.update(89, 10, 12, 2, 3)
        self.assertEqual(r8.id, 89)
        self.assertEqual(r8.width, 10)
        self.assertEqual(r8.height, 12)
        self.assertEqual(r8.x, 2)
        self.assertEqual(r8.y, 3)

    def test_update_method_kwargs(self):
        r9 = Rectangle(4, 5, 1, 1, 30)
        r9.update(width=20, height=25, x=3, y=4)
        self.assertEqual(r9.width, 20)
        self.assertEqual(r9.height, 25)
        self.assertEqual(r9.x, 3)
        self.assertEqual(r9.y, 4)

    def test_to_dictionary(self):
        r10 = Rectangle(4, 5, 1, 1, 40)
        expected_dict = {
            'id': 40,
            'width': 4,
            'height': 5,
            'x': 1,
            'y': 1
        }
        self.assertEqual(r10.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
