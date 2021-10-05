import uuid


class Producto:

    def __init__(self, precio, lote,*args, **kargs):
        self.id = str(uuid.uuid4())
        self.precio = int(precio)
        self.lote = str(lote)

    def str(self):
        return f"{self.id}--{self.precio}--{self.lote}"

    def __repr__(self):
        return 'Soy un Producto'

    def avaluar(self, valor):
        self.precio = valor

    def lotear(self, lote2):
        self.lote = lote2

    def cumple(self, especificacion):
        dict = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict or dict[k] != especificacion.get_value(k):
                return False
        return True