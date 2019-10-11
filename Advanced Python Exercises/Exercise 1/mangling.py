class Coche:

    def __init__(self):
        self.matricula = "1234567V"
        self.motor = "EngineV2"
        self.color = "Red"
        self.propietario = "Pepe"
        self.ruedas = ["wh1", "wh2", "wh3", "wh4"]

    def meth_cambiar_rueda(self):
        pass

    def meth_pintar(self):
        pass

    def meth_vender(self):
        pass

    def __getattr__(self, name):
        meth = 'meth_{0}'.format(name)
        attr = 'attr_{0}'.format(name)

        if attr in self.__dict__:
            return self.__dict__[attr]
        elif meth in self.__dict__:
            return self.__dict__[meth]
        return None

    def __setattr__(self, key, value):
        # Checking if it is a method. A method will have and attribute '__call__'
        if hasattr(value, "__call__"):
            key = "meth_{0}".format(key)
        else:
            key = "attr_{0}".format(key)

        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'vender':
            return
        if item == 'matricula':
            return
        if item == 'propietario':
            return

        meth = 'meth_{0}'.format(item)
        attr = 'attr_{0}'.format(item)

        if hasattr(self, meth):
            super.__delattr__(meth)
        elif hasattr(self, meth):
            super.__delattr__(attr)
        else:
            return


if __name__ == '__main__':

    car = Coche()
    print(car.__dict__)
    print(car.__dir__())
    print(car.matricula)

    # Pruebas añadiendo, quitando cosas etc.
