#!/usr/bin/python3
"""tests Place model."""
import os
import unittest
from models.place import Place


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage Place tests")
class TestPlaceFileStorage(unittest.TestCase):
    """Tests for Place with FileStorage."""

    def tearDown(self):
        try:
            os.remove("file.json")
        except OSError:
            pass

    def test_place_creation(self):
        """Test Place instance creation."""
        p = Place(
            city_id="c1", user_id="u1", name="My house",
            number_rooms=2, price_by_night=100
        )
        self.assertIsNotNone(p.id)
        self.assertEqual(p.name, "My house")
        self.assertEqual(p.number_rooms, 2)
        self.assertEqual(p.price_by_night, 100)

    def test_place_amenity_ids_instance(self):
        """Test Place has amenity_ids as a list."""
        p1 = Place(city_id="c1", user_id="u1", name="P1")
        self.assertIsInstance(p1.amenity_ids, list)


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db", "DBStorage Place tests")
class TestPlaceDBStorage(unittest.TestCase):
    """Tests for Place with DBStorage."""

    def test_place_has_attributes(self):
        """Test Place has expected attributes."""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))