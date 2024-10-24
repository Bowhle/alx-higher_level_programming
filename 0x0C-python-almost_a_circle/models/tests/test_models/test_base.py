# tests/test_models/test_base.py
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_provided(self):
        """Test if the id is correctly assigned when provided."""
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_id_not_provided(self):
        """Test if the id is assigned sequentially when not provided."""
        Base._Base__nb_objects = 0
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)

if __name__ == "__main__":
    unittest.main()
