from typing import List
import unittest
import math
import figures


class TestUM(unittest.TestCase):
    """Unit tests of exercise 7, figures"""

    def setUp(self) -> None:
        print("Executing test of exercise 7: figures")

    def test_square(self) -> None:
        """Init a square and test its functionality"""
        s: figures.Square = figures.Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.width, s.height)
        self.assertIs(s.area(), 25)

    def test_circle(self) -> None:
        """Init a circle and test its functionality"""
        c: figures.Circle = figures.Circle(4)
        self.assertEqual(c.radius, 4)
        self.assertAlmostEqual(c.area(), math.pi*c.radius**2)

    def test_figures_areas(self) -> None:
        """Test the figure area functionality"""
        s: figures.Square = figures.Square(10)
        c: figures.Circle = figures.Circle(10)
        self.assertAlmostEqual(s.area() + c.area(), figures.Figure.areas([s, c]))

    def test_figures_types(self) -> None:
        """Test the figure arch_enemy functionality"""
        s1: figures.Square = figures.Square(10)
        s2: figures.Square = figures.Square(5)
        c1: figures.Circle = figures.Circle(10)
        c2: figures.Circle = figures.Circle(5)
        self.assertFalse(figures.Figure.are_archenemy (s1, c1))
        self.assertFalse(figures.Figure.are_archenemy (c2, s2))
        self.assertTrue(figures.Figure.are_archenemy (c1, c2))
        self.assertTrue(figures.Figure.are_archenemy (s1, s2))


if __name__ == "__main__":
    unittest.main()
