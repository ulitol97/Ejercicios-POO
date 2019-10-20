from typing import List
import unittest
import team


class TestUM(unittest.TestCase):
    """Unit tests of exercise 5, team"""

    def setUp(self) -> None:
        print("Executing test of exercise 5: team")

    def test_person_set_up(self) -> None:
        """Init a person correctly"""
        p: team.Person = team.Person('Name')
        self.assertEqual(p.name, 'Name')

    def test_player_set_up(self) -> None:
        """Init a player with name and number"""
        p: team.Player = team.Player ('Player', 13)
        self.assertEqual(p.name, 'Player')
        self.assertEqual(p.number, 13)
        self.assertEqual(p.__str__(), 'Player: Player - Number: 13')

    def test_coach_set_up(self) -> None:
        """Init a coach with name"""
        c: team.Coach = team.Coach('Name')
        self.assertEqual(c.name, 'Name')

    def test_team_set_up_1(self) -> None:
        """Init team with no additional data"""
        t: team.Team = team.Team()
        self.assertIsNone(t.players)
        self.assertIsNone(t.coach)

    def test_team_set_up_2(self) -> None:
        """Init team with players and coach"""
        players: List[team.Player] = [team.Player('N1', 1), team.Player('N2', 2), team.Player('N3', 3)]
        coach: team.Coach = team.Coach('Coach')
        t: team.Team = team.Team(players, coach)

        self.assertIsNotNone(t.players)
        self.assertIsNotNone(t.coach)
        self.assertIs(len(t.players), 3)


if __name__ == "__main__":
    unittest.main()
