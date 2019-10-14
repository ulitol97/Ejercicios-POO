import unittest
import factorial


class TestUM(unittest.TestCase):
    """Unit tests of exercise 3, factorial"""

    def setUp(self):
        print("Executing test of exercise 3: factorial")

    def test_fact_1(self):
        self.assertEqual(factorial.factorial (5), 120)

    def test_fact_2(self):
        self.assertEqual(factorial.factorial (8), 40320)

    def test_fact_3(self):
        self.assertEqual(factorial.factorial (12), 479001600)

    def test_fact_4(self):
        self.assertEqual(factorial.factorial (15), 1307674368000)


if __name__ == "__main__":
    unittest.main()
