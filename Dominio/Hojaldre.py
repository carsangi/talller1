import uuid

from fabricaPanes.Dominio.Producto import Producto


class Hojaldre(Producto):

    def __init__(self, sabor, forma,precio, lote,*args, **kargs):
        self.sabor = sabor
        self.forma = forma
        super(Hojaldre, self).__init__(precio, lote);

    def str(self):
        return f"{self.id}--{self.sabor}--{self.forma}"

    def __repr__(self):
        return 'Soy un Hojaldre'

    def saborear(self, sabor2):
        self.sabor = sabor2
