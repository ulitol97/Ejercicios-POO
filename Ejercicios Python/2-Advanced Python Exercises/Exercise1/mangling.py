import types


class Coche:
    def __init__(self, matricula, motor, color, propietario, ruedas):
        self.matricula = matricula
        self.motor = motor
        self.color = color
        self.propietario = propietario
        self.ruedas = ruedas

    def meth_cambiar_rueda(self):
        print("Changing wheel")

    def meth_pintar(self):
        print("Painted")

    def meth_vender(self, propietario):
        print("Selling car to {}".format(propietario))
        self.propietario = propietario

    def __setattr__(self, name, value):
        if hasattr(value, '__call__'):
            name = "meth_{}".format(name)
        else:
            name = "attr_{}".format(name)
        super().__setattr__(name, value)

    def __getattr__(self, name):
        meth = "meth_{}".format(name)
        attr = "attr_{}".format(name)

        if attr in self.__dict__:
            return self.__dict__[attr]
        if meth in self.__dir__():
            # Principal diferencia
            return super().__getattribute__(meth)
        return None

    def __delattr__(self, item):
        if item == 'vender':
            return
        if item == 'matricula':
            return
        if item == 'propietario':
            return

        meth = "meth_{}".format(item)
        attr = "attr_{}".format(item)
        if hasattr(self, meth):
            super().__delattr__(meth)
        elif hasattr(self, attr):
            super().__delattr__(attr)
        else:
            return


if __name__ == '__main__':
    """Sample main to test functionality. Create a car an add some attrs and methods, etc."""

    c = Coche('1234567V', 'EngineV2', 'Red', 'Edu', ['r1', 'r2', 'r3', 'r4'])
    print(c.matricula)
    print([f for f in dir(c) if not f.startswith('__')])
    c.combustible = "barato"
    print([f for f in dir(c) if not f.startswith('__')])
    print(c.combustible)
    c.acelera = lambda: print("acelera mucho")
    print([f for f in dir(c) if not f.startswith('__')])
    c.acelera()

    del c.vender
    del c.acelera
    del c.matricula
    print([f for f in dir(c) if not f.startswith('__')])

    mi_funcion = lambda self: print("soy {}".format(self.attr_matricula))
    c.identificate = types.MethodType(mi_funcion, c)
    c.identificate()

    mi_funcion = lambda self: print("soy {}".format(getattr(self, 'matricula')))
    c.identificate_v2 = types.MethodType(mi_funcion, c)
    c.identificate_v2()
    print([f for f in dir(c) if not f.startswith('__')])
