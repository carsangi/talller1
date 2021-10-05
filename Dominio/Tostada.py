import uuid

from fabricaPanes.Dominio.Producto import Producto


class Tostada(Producto):

    def __init__(self, sabor, tipo,precio,lote,*args, **kargs):
        self.sabor = sabor
        self.tipo = tipo
        super(Tostada, self).__init__(precio,lote);

    def str(self):
        return f"{self.id}--{self.sabor}--{self.tipo}--{self.precio}--{self.lote}"

    def __repr__(self):
        return 'Soy un Tostada'

    def tipar(self, tipar):
        self.tipo = tipar
