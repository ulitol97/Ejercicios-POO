from typing import List, Optional


class Person:
    """Parent class for players and coaches, who have a name attribute"""

    def __init__(self, name: str) -> None:
        self.name: str = name


class Player(Person):
    """Represents a player with a name and a number"""

    def __init__(self, name: str, number: int) -> None:
        super().__init__(name)
        self.number: int = number

    def __str__(self) -> str:
        return 'Player: {0} - Number: {1}'.format(self.name, self.number)


class Coach(Person):
    """Represents a coach with a name"""

    def __init__(self, name: str) -> None:
        super().__init__(name)


class Team:
    """Represents a Team with a list of players"""

    def __init__(self, players: List[Player] = None, coach: Coach = None) -> None:
        self.players: Optional[List[Player]] = players
        self.coach: Optional[Coach] = coach

    def __str__(self) -> str:
        ret: str = ''
        if not (self.coach is None):
            ret += 'Coach:\n\t{0}\nPlayers:\n'.format(self.coach.name)
        if not (self.players is None):
            for player in self.players:
                ret += '\t' + player.__str__() + '\n'
        return ret


if __name__ == "__main__":
    """Sample main to test functionality. Create a list of players and a coach.
    Init a team and print its members"""

    # Create a list of players simulating a LoL team
    adcarry: Player = Player("Carry", 1)
    support: Player = Player("Support", 2)
    jungler: Player = Player("Jungle", 3)
    top:Player = Player("Top", 4)
    mid: Player = Player("Mid", 5)

    players: List[Player] = [top, jungler, mid, adcarry, support]
    # Create a coach
    coach: Coach = Coach('Xpeke')

    # Create a team given the list of players and a coach
    my_team: Team = Team(players, coach)
    print(my_team)
