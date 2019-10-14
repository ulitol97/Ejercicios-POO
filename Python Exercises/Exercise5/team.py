class Person:
    """Parent class for players and coaches, who have a name attribute"""
    def __init__(self, name):
        self.name = name


class Player (Person):
    """Represents a player with a name and a number"""
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number

    def __str__(self):
        return 'Player: {0} - Number: {1}'.format(self.name, self.number)


class Coach(Person):
    """Represents a coach with a name"""
    def __init__(self, name):
        super().__init__(name)


class Team:
    """Represents a Team with a list of players"""
    def __init__(self, players=None, coach=None):
        self.players = players
        self.coach = coach

    def __str__(self):
        ret = 'Coach:\n\t{0}\nPlayers:\n'.format(self.coach.name)
        for player in self.players:
            ret += '\t'+player.__str__()+'\n'
        return ret


if __name__ == "__main__":
    """Sample main to test functionality. Create a list of players and a coach.
    Init a team and print its members"""

    # Create a list of players simulating a LoL team
    adcarry = Player("Carry", 1)
    support = Player("Support", 2)
    jungler = Player("Jungle", 3)
    top = Player("Top", 4)
    mid = Player("Mid", 5)

    players = [top, jungler, mid, adcarry, support]
    # Create a coach
    coach = Coach('Xpeke')

    # Create a team given the list of players and a coach
    my_team = Team(players, coach)
    print(my_team)
