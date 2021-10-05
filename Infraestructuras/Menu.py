import os

from fabricaPanes.Dominio.EspecificacionProducto import EspecificacionProducto
from fabricaPanes.Dominio.InventarioProductos import InventarioProductos
from fabricaPanes.Infraestructuras.PersistenciaProducto import PersistenciaProducto


class Menu:
    def buscar_producto(self):
        saver = PersistenciaProducto()
        inventario = InventarioProductos()
        espec = EspecificacionProducto()
        '''for file in os.listdir("./Files"):
            if '.json' in file:
                inventario.agregar_objeto(saver.load_json(file))'''


        valor = int(input("Ingrese el valor por el cual buscar producto: \n"
                          "1. ID \n"
                          "2. Precio \n"
                          "3. Lote \n"))
        if valor==1:
            id = input("Ingrese el id \n")
            espec.agregar_parametro('id', id)
            if len(list(inventario.buscar(espec))) == 0:
                print("No hay producto registrado con ese id")
            else:
                print(list(inventario.buscar(espec)))
        if valor==2:
            precio = int(input("Ingrese el precio \n"))
            espec.agregar_parametro('precio', precio)
            if len(list(inventario.buscar(espec))) == 0:
                print("No hay producto registrado con ese precio")
            else:
                print(list(inventario.buscar(espec)))
        if valor==3:
            lote = input("Ingrese el lote \n")
            espec.agregar_parametro('lote', lote)
            print(espec)
            if len(list(inventario.buscar(espec))) == 0:
                print(inventario.buscar(espec))
                print("No hay producto registrado con ese lote")
            else:
                print(list(inventario.buscar(espec)))