import unittest
import even_or_odd


class TestUM(unittest.TestCase):
    """Unit tests of exercise 3, even or odd"""

    def setUp(self):
        print("Executing test of exercise 3: even or odd")

    def test_even_1(self):
        self.assertTrue(even_or_odd.even(4))

    def test_even_2(self):
        self.assertTrue(even_or_odd.even(8458))

    def test_odd_1(self):
        self.assertFalse(even_or_odd.even(5))

    def test_odd_2(self):
        self.assertFalse(even_or_odd.even(3851))


if __name__ == "__main__":
    unittest.main()
