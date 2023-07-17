#!/usr/bin/python3
"""Module to test the Square class"""

import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """A class to test the Square class"""
    def setUp(self):
        """Resets the number of objects"""
        Base._Base__nb_objects = 0

    # ---------------------------Tests for width-------------------------
    def test_width(self):
        """Test for width"""
        # assertEquals Test for width
        s1 = Square(10)
        self.assertEqual(s1.width, 10)
        s2 = Square(2)
        self.assertEqual(s2.width, 2)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.width, 8)
        s4 = Square(*[2, 4, 12, 9, 1])
        self.assertEqual(s4.width, 2)

        # assertRaises Test for width
        # TypeError: width must be an integer
        self.assertRaises(TypeError, Square, *["1", 2, 3, 4])
        self.assertRaises(TypeError, Square, *[{0}, 2, 3, 4])
        self.assertRaises(TypeError, Square, *[[1], 2, 3, 4])
        self.assertRaises(TypeError, Square, *[(1,), 2, 3, 4])
        self.assertRaises(TypeError, Square, *[None, 2, 3, 4])
        # ValueError: width must be > 0
        self.assertRaises(ValueError, Square, *[-1, 2, 3, 4])
        self.assertRaises(ValueError, Square, *[0, 2, 3, 4])
        self.assertRaises(ValueError, Square, *[-999999, 2, 3, 4])

    # ---------------------------Tests for height-------------------------
    def test_height(self):
        """Test for height"""
        # assertEquals Test for height
        s1 = Square(10)
        self.assertEqual(s1.height, 10)
        s2 = Square(2)
        self.assertEqual(s2.height, 2)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.height, 8)
        s4 = Square(2, 4, 12, 9, 1)
        self.assertEqual(s4.height, 2)

        # assertRaises Test for height
        # TypeError: height must be an integer
        self.assertRaises(TypeError, Square, *[1, "2", 3, 4])
        self.assertRaises(TypeError, Square, *[1, {0}, 3, 4])
        self.assertRaises(TypeError, Square, *[1, [2], 3, 4])
        self.assertRaises(TypeError, Square, *[1, (2,), 3, 4])
        self.assertRaises(TypeError, Square, *[1, None, 3, 4])
