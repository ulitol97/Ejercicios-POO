import unittest
import calculate_marks


class TestUM(unittest.TestCase):
    """Unit tests of exercise 6, calculate marks"""

    def setUp(self):
        print("Executing test of exercise 6: calculate marks")

    def test_marks_1(self):
        """Compute some marks and check the result"""
        solutions = {1: 'a', 2: 'b'}
        # Student 1 gets 0.75 and student 2 gets 2 points
        answers = {1: {1: 'a', 2: 'c'}, 2: {1: 'a', 2: 'b'}}

        results = calculate_marks.calculate_marks(solutions, answers)

        self.assertEqual(results[1], 0.75)
        self.assertEqual(results[2], 2)

    def test_marks_2(self):
        """Compute some marks and check the result"""
        solutions = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        # Student 1 gets 2.75 and student 2 gets 3 points (left 1 blank question)
        answers = {1: {1: 'a', 2: 'c', 3: 'c', 4: 'd'}, 2: {1: 'a', 2: 'b', 4: 'd'}}

        results = calculate_marks.calculate_marks(solutions, answers)

        self.assertEqual(results[1], 2.75)
        self.assertEqual(results[2], 3)




if __name__ == "__main__":
    unittest.main()
