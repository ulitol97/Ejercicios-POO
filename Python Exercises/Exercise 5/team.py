class Person:
    def __init__(self, name):
        self.name = name


class Player (Person):

    def __init__(self, name, number):
        super().__init__(name)
        self.number = number


class Coach(Person):

    def __init__(self, name):
        super().__init__(name)


class Team:

    def __init__(self):
        self.players = []


if __name__ == "__main__":
    my_team = Team()
    adcarry = Player ("Carry", 1)
    support = Player ("Support", 2)
    jungler = Player ("Jungle", 3)
    top = Player ("Top", 4)
    mid = Player ("Mid", 5)
    my_team.players.append(adcarry)
    my_team.players.append(support)
    my_team.players.append(jungler)
    my_team.players.append(top)
    my_team.players.append(mid)

    for i in range(len(my_team.players)):
        print("Position: {0} - Number: {1}".format(my_team.players[i].name, my_team.players[i].number))
