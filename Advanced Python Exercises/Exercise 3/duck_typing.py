# El treeset es un set y por tanto ordenado. Al meterle una persona debe saber como compararlas.
# Necesitamos implementar el Compare() en persona


class Person:

    def __init__(self, name, surname, age=18, dni='1234567V'):
        self.name = name
        self.surname = surname
        self.age = age
        self.dni = dni

    def compare_to(self, person):
        if self.surname >= person.surname:
            return 1
        else:
            return -1


class TreeSet:

    def __init__(self, comparator=None):
        self.contents = []  # Implemented as an array for simplicity
        self.comparator = comparator

    def add(self, person):

        if len(self.contents) == 0:
            self.contents.append(person)
            return

        # No specific comparator
        if self.comparator is None:
            for i in range(0, len(self.contents)):
                if person.compare_to(self.contents[i]) == -1:
                    self.contents.insert(i, person)
                    return
            else:
                self.contents.append(person)

        else:
            for i in range(0, len(self.contents)):
                if self.comparator.compare(person, self.contents[i]) == -1:
                    self.contents.insert(i, person)
                    return
            else:
                self.contents.append(person)

    def __str__(self):
        ret = "["
        for p in self.contents:
            ret += "[{0}]".format(p.name)
        return ret + "]"


if __name__ == '__main__':
    tree_set = TreeSet()
    person = Person ("Edu", "Ulibarri")
    person1 = Person ("Alex", "ZZZ")
    person2 = Person ("Marcial", "ZZZ")
    tree_set.add(person)
    tree_set.add(person1)
    tree_set.add(person2)
    print (tree_set)
    print (type(TreeSet))