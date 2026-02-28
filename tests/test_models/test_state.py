#!/usr/bin/python3
"""Tests for State model."""
import os
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class."""

    def tearDown(self):
        try:
            os.remove("file.json")
        except OSError:
            pass

    def test_state_creation(self):
        """Test State instance creation."""
        s = State(name="California")
        self.assertIsNotNone(s.id)
        self.assertEqual(s.name, "California")

    def test_state_inherits_base_model(self):
        """Test State inherits BaseModel attributes."""
        s = State(name="Texas")
        self.assertIsNotNone(s.created_at)
        self.assertIsNotNone(s.updated_at)

    def test_state_to_dict(self):
        """Test State to_dict method."""
        s = State(name="Oregon")
        d = s.to_dict()
        self.assertEqual(d["__class__"], "State")
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)

    def test_state_str(self):
        """Test State __str__ method."""
        s = State(name="Nevada")
        result = str(s)
        self.assertIn("State", result)
        self.assertIn(s.id, result)

    def test_state_name_attribute(self):
        """Test State name attribute."""
        s = State()
        s.name = "Florida"
        self.assertEqual(s.name, "Florida")


if __name__ == "__main__":
    unittest.main()
