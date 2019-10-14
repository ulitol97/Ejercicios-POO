import types
import unittest
import mangling


class TestUM(unittest.TestCase):
    """Unit tests of advanced exercise 1, mangling"""

    def setUp(self):
        print("Executing test of advanced exercise 1: mangling")

    def test_car_set_up(self):
        """Init a car and check the attribute names have been stored correctly, "vender" cannot be deleted
        and the methods work"""
        c = mangling.Coche('1234567V', 'EngineV2', 'Red', 'Edu', ['r1', 'r2', 'r3', 'r4'])
        # External access
        self.assertEqual(c.matricula, '1234567V')
        self.assertEqual(c.motor, 'EngineV2')
        self.assertEqual(c.color, 'Red')
        self.assertEqual(c.propietario, 'Edu')
        self.assertEqual(c.ruedas, ['r1', 'r2', 'r3', 'r4'])

        # Internal access
        properties = dir(c)
        self.assertTrue('attr_matricula' in properties)
        self.assertTrue('attr_motor' in properties)
        self.assertTrue('attr_color' in properties)
        self.assertTrue('attr_propietario' in properties)
        self.assertTrue('attr_ruedas' in properties)

        # Cannot delete "vender"
        self.assertTrue('meth_vender' in properties)
        del c.vender
        self.assertTrue('meth_vender' in properties)
        # Sell car
        c.vender('Toni')
        self.assertEqual(c.propietario, 'Toni')

    def test_car(self):
        """Init a car and check attributed and methods can be added and follow the correct nomenclature"""
        c = mangling.Coche('1234567V', 'EngineV2', 'Red', 'Edu', ['r1', 'r2', 'r3', 'r4'])
        c.precio = 4000
        self.assertIs(c.precio, 4000)
        self.assertTrue('attr_precio' in dir(c))

        sample_method = lambda self: print("I am a new method.")
        c.method = types.MethodType(sample_method, c)
        self.assertTrue('meth_method' in dir(c))


if __name__ == "__main__":
    unittest.main()
