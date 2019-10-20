from typing import List
import math


class Figure:
    """Template figure class"""
    def area(self):
        pass

    @staticmethod
    def areas (figures) -> float:
        """Get the total area of a list of figures"""
        total_area: float = 0
        for figure in figures:
            total_area += figure.area()
        return total_area

    @staticmethod
    def are_archenemy (figure1, figure2) -> bool:
        """Say if figure 1 and figure2 are figures and have the same type"""
        return isinstance(figure1, Figure) and isinstance(figure2, Figure) and figure1.__class__ == figure2.__class__


class Square (Figure):
    """Class representing a Square, which is a Figure"""
    def __init__(self, side_length: float) -> None:
        super().__init__()
        self.width: float = side_length
        self.height: float = side_length

    def area(self) -> float:
        return self.width*self.height


class Circle (Figure):
    """Class representing a Circle, which is a Figure"""
    def __init__(self, radius: float) -> None:
        super().__init__()
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * self.radius**2


if __name__ == "__main__":
    """Sample main to test functionality. Create a different figures and check its methods and types"""
    c1: Circle = Circle(2)
    print("Circle 1 area: {}".format(c1.area()))
    c2: Circle = Circle(3)
    print("Circle 2 area: {}".format(c2.area()))
    s1: Square = Square(2)
    print("Square 1 area: {}".format(s1.area()))
    s2: Square = Square(3)
    print("Square 2 area: {}".format(s2.area()))

    print("Total area of the four figures: {}".format(Figure.areas([c1, c2, s1, s2])))

    print('Testing classes equality:')
    print(Figure.are_archenemy(s1, s2))
    print(Figure.are_archenemy(s1, c2))