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


class ComparatorDNI:

    def compare(self, person1, person2):
        if person1.dni >= person2.dni:
            return 1
        else:
            return -1


class ComparatorAge:

    def compare(self, person1, person2):
        if person1.age >= person2.age:
            return 1
        else:
            return -1


if __name__ == '__main__':
    tree_set = TreeSet()  # Standard tree set
    tree_set_dni = TreeSet()  # Tree set comparing by DNI
    tree_set_age = TreeSet()  # Tree set comparing by age

    p1 = Person("Edu", "A", 21)
    p2 = Person("Alex", "B", 22)
    p3 = Person("Marcial", "C", 23)

    tree_set.add(p1)
    tree_set.add(p2)
    tree_set.add(p3)

    print(tree_set)
    print(type(TreeSet))
