from fabricaPanes.Dominio.Producto import Producto


class Pan(Producto):

    def __init__(self, tipo, gusto, precio, lote,*args, **kargs):
        self.tipo = tipo
        self.gusto = gusto
        super(Pan, self).__init__(precio, lote);

    def str(self):
        return f"{self.id}--{self.tipo}--{self.gusto}"

    def __repr__(self):
        return 'Soy un Pan'

    def gustar(self, gustar):
        self.gusto = gustar