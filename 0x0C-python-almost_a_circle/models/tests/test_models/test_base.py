# tests/test_models/test_base.py
import unittest
import os
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

    def test_load_from_file_nonexistent(self):
        """Test loading from a non-existent file."""
        # Ensure the file does not exist
        filename = "Base.json"
        if os.path.isfile(filename):
            os.remove(filename)
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_existing(self):
        """Test loading from an existing file with data."""
        # Setup: create a file with sample data
        sample_data = [{'id': 1}, {'id': 2}]
        with open("Base.json", 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(sample_data))

        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

        # Cleanup: remove the test file
        if os.path.isfile("Base.json"):
            os.remove("Base.json")


if __name__ == "__main__":
    unittest.main()
