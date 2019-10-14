import unittest
import figures


class TestUM(unittest.TestCase):
    """Unit tests of exercise 7, figures"""

    def setUp(self):
        print("Executing test of exercise 7: figures")

    def test_square(self):
        """Try to init a person without name"""
        with self.assertRaises(TypeError):
            p = team.Person()

    def test_circle(self):
        """Init a person correctly"""
        p = team.Person('Name')
        self.assertEqual(p.name, 'Name')

    def test_figures_areas(self):
        """Init a player with name and number"""
        p = team.Player ('Player', 13)
        self.assertEqual(p.name, 'Player')
        self.assertEqual(p.number, 13)
        self.assertEqual(p.__str__(), 'Player: Player - Number: 13')

    def test_figures_types(self):
        """Init a coach with name"""
        c = team.Coach('Name')
        self.assertEqual(c.name, 'Name')


if __name__ == "__main__":
    unittest.main()
