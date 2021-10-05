from fabricaPanes.Dominio.EspecificacionProducto import EspecificacionProducto
from fabricaPanes.Dominio.Pan import Pan
from fabricaPanes.Dominio.Galleta import Galleta
from fabricaPanes.Dominio.Hojaldre import Hojaldre
from fabricaPanes.Dominio.Dulce import Dulce
from fabricaPanes.Dominio.Tostada import Tostada


class InventarioProductos():

    def __init__(self):
        self.productos = []

    def agregar_Producto(self,producto):
        if isinstance(producto,Hojaldre):
            espec = EspecificacionProducto()
            espec.agregar_parametro('id', producto.id)
            if len(list(self.buscar(espec))) == 0:
                self.productos.append(producto)
            else:
                raise Exception('Hojaldre repetido')
        elif isinstance(producto,Dulce):
            espec = EspecificacionProducto()
            espec.agregar_parametro('id', producto.id)
            if len(list(self.buscar(espec))) == 0:
                self.productos.append(producto)
            else:
                raise Exception('Dulce repetido')
        elif isinstance(producto,Tostada):
            espec = EspecificacionProducto()
            espec.agregar_parametro('id', producto.id)
            if len(list(self.buscar(espec))) == 0:
                self.productos.append(producto)
            else:
                raise Exception('Tostada repetido')
        elif isinstance(producto,Pan):
            espec = EspecificacionProducto()
            espec.agregar_parametro('id', producto.id)
            if len(list(self.buscar(espec))) == 0:
                self.productos.append(producto)
            else:
                raise Exception('Pan repetido')
        elif isinstance(producto,Galleta):
            espec = EspecificacionProducto()
            espec.agregar_parametro('id', producto.id)
            if len(list(self.buscar(espec))) == 0:
                self.productos.append(producto)
            else:
                raise Exception('Galleta repetido')

    def buscar(self,especificacion):

        for h in self.productos:
            if h.cumple(especificacion):
                yield h