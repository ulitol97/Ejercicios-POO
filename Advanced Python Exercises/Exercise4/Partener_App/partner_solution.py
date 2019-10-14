from datetime import datetime
"""Este fichero .py contiene mi solución capaz de pasar los tests que me pasó mi compañeró y que están en
'partner_test.py'"""

class Location:
    """Documentación de Location, que debe exceder los 30 caracteres..."""
    def __init__(self, x=None, y=None):
        self.x = x or 0.0
        self.y = y or 0.0

    def __str__(self):
        return "x:{0} y:{1}".format(self.x, self.y)

class Jugador:
    """Documentación de Jugador, que debe exceder los 30 caracteres..."""

    def __init__(self):
        self.vida = 100
        self.location = Location()

    def teletransportar(self, location):
        self.location = location

    def comer(self, cantidad):
        pass
