from fabricaPanes.Dominio.Producto import Producto


class Galleta(Producto):

    def __init__(self, relleno, color,precio,lote,*args, **kargs):
        self.id = '12345'
        self.relleno = relleno
        self.color = color
        super(Galleta, self).__init__(precio, lote);

    def str(self):
        return f"{self.id}--{self.relleno}--{self.color}"

    def __repr__(self):
        return 'Soy una Galleta'

    def rellenar(self, rellenar):
        self.relleno = rellenar