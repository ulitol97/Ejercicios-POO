import unittest
import prime_factors


class TestUM(unittest.TestCase):
    """Unit tests of exercise 4, prime factors"""

    def setUp(self):
        print("Executing test of exercise 4: prime factors")

    def test_prime_factors_1(self):
        self.assertEqual(prime_factors.get_prime_factors (25), [5])

    def test_prime_factors_2(self):
        self.assertEqual(prime_factors.get_prime_factors (952), [2, 7, 17])

    def test_prime_factors_3(self):
        self.assertEqual(prime_factors.get_prime_factors (4), [2])

    def test_prime_factors_4(self):
        self.assertEqual(prime_factors.get_prime_factors (1000), [2, 5])


if __name__ == "__main__":
    unittest.main()
