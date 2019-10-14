import unittest
import is_prime


class TestUM(unittest.TestCase):
    """Unit tests of exercise 4, prime numbers"""

    def setUp(self):
        print("Executing test of exercise 4: prime numbers")

    def test_prime_1(self):
        self.assertTrue(is_prime.is_prime (5))

    def test_prime_2(self):
        self.assertTrue(is_prime.is_prime (83))

    def test_prime_3(self):
        self.assertFalse(is_prime.is_prime (85))

    def test_prime_4(self):
        self.assertFalse(is_prime.is_prime (1200))


if __name__ == "__main__":
    unittest.main()
