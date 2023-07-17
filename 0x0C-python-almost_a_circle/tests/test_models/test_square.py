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
        self.assertEqual(s2.height, 2)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.width, 8)
        self.assertEqual(s3.height, 8)

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

    def test_x(self):
        """Test for x"""
        # assertEquals Test for x
        s1 = Square(10)
        self.assertEqual(s1.x, 0)
        s2 = Square(2, 3)
        self.assertEqual(s2.x, 3)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.x, 0)
        s4 = Square(2, 4, 12, 9, 1)
        self.assertEqual(s4.x, 4)

        # assertRaises Test for x
        # TypeError: x must be an integer
        self.assertRaises(TypeError, Square, *[1, 2, "3", 4])
        self.assertRaises(TypeError, Square, *[1, 2, {0}, 4])
        self.assertRaises(TypeError, Square, *[1, 2, [3], 4])
        self.assertRaises(TypeError, Square, *[1, 2, (3,), 4])
        self.assertRaises(TypeError, Square, *[1, 2, None, 4])
        # ValueError: x must be >= 0
        self.assertRaises(ValueError, Square, *[1, 2, -1, 4])

    def test_y(self):
        """Test for y"""
        # assertEquals Test for y
        s1 = Square(10)
        self.assertEqual(s1.y, 0)
        s2 = Square(2, 3, 4)
        self.assertEqual(s2.y, 4)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.y, 0)
        s4 = Square(2, 4, 12, 9, 1)
        self.assertEqual(s4.y, 12)

        # assertRaises Test for y
        # TypeError: y must be an integer
        self.assertRaises(TypeError, Square, *[1, 2, 3, "4"])
        self.assertRaises(TypeError, Square, *[1, 2, 3, {4}])
        self.assertRaises(TypeError, Square, *[1, 2, 3, [4]])
        self.assertRaises(TypeError, Square, *[1, 2, 3, (4,)])
        self.assertRaises(TypeError, Square, *[1, 2, 3, None])
        # ValueError: y must be >= 0
        self.assertRaises(ValueError, Square, *[1, 2, 3, -4])

    # ---------------------------Tests for id-------------------------
    def test_id(self):
        """Test for id"""
        # assertEquals Test for id
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        s2 = Square(2, 3)
        self.assertEqual(s2.id, 2)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.id, 12)
        s4 = Square(2, 4, 12, 9, 1)
        self.assertEqual(s4.id, 1)

        # assertRaises Test for id
        # TypeError: id must be an integer
        self.assertRaises(TypeError, Square, *[1, 2, 3, 4.0])
        self.assertRaises(TypeError, Square, *[1, 2, 3, {4}])
        self.assertRaises(TypeError, Square, *[1, 2, 3, [4]])
        self.assertRaises(TypeError, Square, *[1, 2, 3, (4,)])
        self.assertRaises(TypeError, Square, *[1, 2, 3, None])
        # ValueError: id must be >= 0
        self.assertRaises(ValueError, Square, *[1, 2, 3, -4])
