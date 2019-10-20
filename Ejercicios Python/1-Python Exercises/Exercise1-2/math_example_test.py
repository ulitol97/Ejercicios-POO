import unittest
import math_example


class TestUM(unittest.TestCase):
    """Part of exercise 1, where we test the functionality of an example Math class"""
    def setUp(self):
        self.testClass = math_example.Math()
        print("Executing test of example class: Math")

    def test_mul_1(self):
        self.assertEqual(self.testClass.mul(3, 4), 12)

    def test_mul_2(self):
        self.assertRaises(ValueError, self.testClass.mul, "a", 4)

    def test_equal_1(self):
        self.assertFalse(self.testClass.equal(3, 4), "I failed...")

    def test_equal_2(self):
        self.assertTrue(self.testClass.equal(3, 3), "I failed...")

    def test_equal_3(self):
        self.assertFalse(self.testClass.equal('3', 3))

    def test_equal_4(self):
        self.assertTrue(self.testClass.equal('a', 'a'))

    def test_equal_5(self):
        self.assertFalse(self.testClass.equal('3', 'a'))


if __name__ == "__main__":
    unittest.main()
