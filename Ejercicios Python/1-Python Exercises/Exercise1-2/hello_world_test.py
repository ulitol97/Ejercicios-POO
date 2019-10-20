import unittest
import hello_world


class TestExercise1(unittest.TestCase):
    """Part of exercise 2, where we test the functionality of exercise 1"""
    def setUp(self) -> None:
        self.testClass = hello_world.Program()
        print("Executing test of Exercise 1")

    def test_hello_world(self) -> None:
        self.assertEqual(self.testClass.run(), 'Hello Master!!')


if __name__ == "__main__":
    unittest.main()
