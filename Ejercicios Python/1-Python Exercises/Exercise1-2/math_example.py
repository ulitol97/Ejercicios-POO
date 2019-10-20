class Math:
    def mul(self, param, param1):
        try:
            float(param)
            float(param1)
        except ValueError:
            raise ValueError("Can't multiply non-numbers")
        return param * param1

    def equal(self, param, param1):
        return param == param1
