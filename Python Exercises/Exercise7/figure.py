import math


class Figure:
    """Template figure class"""
    def area(self):
        pass

    @staticmethod
    def areas (figures):
        """Get a list with the areas of a list of figures"""
        areas = []
        for figure in figures:
            areas.append(figure.area())
        return areas

    @staticmethod
    def are_archenemy (figure1, figure2):
        """Say if figure 1 and figure2 are figures and have the same type"""
        return isinstance(figure1, Figure) and isinstance(figure2, Figure) and figure1.__class__ == figure2.__class__


class Square (Figure):
    def __init__(self, side_length):
        super().__init__()
        self.width = side_length
        self.height = side_length

    def area(self):
        return self.width*self.height


class Circle (Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


if __name__ == "__main__":
    c1 = Circle(2)
    c2 = Circle(3)
    s1 = Square(2)
    s2 = Square(3)

    print (c1.area())
    print (c2.area())
    print (s1.area())
    print (s2.area())
    print(Figure.are_archenemy(s1, c2))