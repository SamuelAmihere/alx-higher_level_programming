#!/usr/bin/python3
"""Module for unittesting the Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """A class for unittesting the Base class"""
    def setUp(self):
        """Resets the number of objects"""
        Base._Base__nb_objects = 0

    # Test for private class attributes
    # Test for __nb_objects
    def test_id(self):
        """Test for id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

        b5 = Base(12)
        b6 = Base()
        self.assertEqual(b5.id, 12)
        self.assertEqual(b6.id, 5)

        b7 = Base("3")
        self.assertEqual(b7.id, "3")

    # Test for private class attributes access
    def test_private_class_attributes_access(self):
        """Test for private class attributes access"""
        b = Base()
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    # -------------test for static methods---------------
    # test for to_json_string
    def test_to_json_string(self):
        """Test for to_json_string"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')
        self.assertEqual(Base.to_json_string([{"id": 12}, {"id": 13}]),
                         '[{"id": 12}, {"id": 13}]')

    # test for from_json_string
    def test_from_json_string(self):
        """Test for from_json_string"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'),
                         [{"id": 12}])
        self.assertEqual(Base.from_json_string('[{"id": 12}, {"id": 13}]'),
                         [{"id": 12}, {"id": 13}])

    # test for create
    def test_create(self):
        """Test for create"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 3/5")

        r3 = Rectangle(3, 5, 1, 2, 12)
        r3_dictionary = r3.to_dictionary()
        r4 = Rectangle.create(**r3_dictionary)
        self.assertEqual(r3 == r4, False)
        self.assertEqual(r3 is r4, False)
        self.assertEqual(r3.__str__(), "[Rectangle] (12) 1/2 - 3/5")
        self.assertEqual(r4.__str__(), "[Rectangle] (12) 1/2 - 3/5")

        # test for create square
        s1 = Square(3, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1 == s2, False)
        self.assertEqual(s1 is s2, False)
        self.assertEqual(s1.__str__(), "[Square] (2) 1/0 - 3")
        self.assertEqual(s2.__str__(), "[Square] (2) 1/0 - 3")
