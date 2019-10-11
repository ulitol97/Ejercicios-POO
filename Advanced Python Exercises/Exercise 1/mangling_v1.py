class Coche:
    def __init__(self,matricula,motor,propietario,ruedas):
        self.matricula = matricula
        self.motor = motor
        self.propietario = propietario
        self.ruedas = ruedas

    def meth_cambiar_rueda(self):
        print("Cambiando rueda")

    def meth_pintar(self):
        print("Pintando")

    def meth_vender(self, propietario):
        print("Vendiendo coche a {0}".format(propietario))
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



c = Coche('m1','m2','paco',['r1', 'r2', 'r3', 'r4'])
print(c.__dict__)
print(c.__dir__())
c.vender('antonio')
print(c.propietario)


