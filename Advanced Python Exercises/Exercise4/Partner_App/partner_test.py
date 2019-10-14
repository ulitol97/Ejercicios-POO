"""Parte del ejercicio 4. Debajo están los test unitarios que me pasó un compañero para crear una estructura de
clases que los pasen. Mi solución a los tests del compañero están en 'partner_solution.py'"""

import unittest
import partner_solution


class TestUM(unittest.TestCase):

    def test_imports(self):
        self.assertTrue('partner_solution' in globals().keys())

    def test_classes(self):
        self.assertTrue(hasattr(partner_solution, 'Jugador'))
        self.assertTrue(hasattr(partner_solution, 'Location'))

    def test_documentation(self):
        self.assertTrue(partner_solution.Jugador.__doc__ is not None)
        self.assertTrue(partner_solution.Location.__doc__ is not None)
        self.assertTrue(len(partner_solution.Jugador.__doc__) > 30)
        self.assertTrue(len(partner_solution.Location.__doc__) > 30)

    def test_1(self):
        from types import FunctionType
        self.assertTrue(partner_solution.Jugador.__dict__['teletransportar'] is not None)
        self.assertTrue('__call__' in dir(partner_solution.Jugador.teletransportar))
        self.assertTrue(isinstance(partner_solution.Jugador.__dict__['teletransportar'], FunctionType))
        self.assertTrue('location' in partner_solution.Jugador.teletransportar.__code__.co_varnames)

    def test_2(self):
        var = partner_solution.Jugador()
        self.assertTrue(hasattr(var, 'vida'))
        self.assertTrue(isinstance(var.vida, int))
        self.assertTrue(hasattr(var, 'location'))
        self.assertTrue(isinstance(var.location, partner_solution.Location))

    def test_3(self):
        var = partner_solution.Jugador().location
        self.assertTrue(hasattr(var, 'x'))
        self.assertTrue(hasattr(var, 'y'))
        self.assertTrue(isinstance(var.x, float))
        self.assertTrue(isinstance(var.y, float))

    def test_4(self):
        from types import FunctionType
        self.assertTrue(partner_solution.Jugador.__dict__['comer'] is not None)
        self.assertTrue('__call__' in dir(partner_solution.Jugador.comer))
        self.assertTrue(isinstance(partner_solution.Jugador.__dict__['comer'], FunctionType))
        self.assertTrue('cantidad' in partner_solution.Jugador.comer.__code__.co_varnames)

    def test_5(self):
        var = partner_solution.Jugador()
        self.assertTrue(var.location.__str__() == "x:0.0 y:0.0")
        var.teletransportar(partner_solution.Location(1.3, 2.3))
        self.assertTrue(var.location.__str__() == "x:1.3 y:2.3")

    def test_6(self):
        self.assertTrue("x" in partner_solution.Location.__init__.__code__.co_varnames)
        self.assertTrue("y" in partner_solution.Location.__init__.__code__.co_varnames)


if __name__ == '__main__':
    unittest.main()