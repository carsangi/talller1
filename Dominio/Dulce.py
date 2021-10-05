from fabricaPanes.Dominio.Producto import Producto


class Dulce(Producto):

    def __init__(self, tipo, sabor,precio,lote,*args, **kargs):
        self.id = '12345'
        self.tipo = tipo
        self.sabor = sabor
        super(Dulce, self).__init__(precio, lote);

    def str(self):
        return f"{self.id}--{self.tipo}--{self.sabor}"

    def __repr__(self):
        return 'Soy un Dulce'

    def saborizar(self, saborizar):
        self.sabor = saborizar