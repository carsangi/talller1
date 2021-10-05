import os

from fabricaPanes.Dominio.Dulce import Dulce
from fabricaPanes.Dominio.Galleta import Galleta
from fabricaPanes.Dominio.Hojaldre import Hojaldre
from fabricaPanes.Dominio.InventarioProductos import InventarioProductos
from fabricaPanes.Dominio.Pan import Pan
from fabricaPanes.Dominio.Tostada import Tostada
from fabricaPanes.Infraestructuras.Menu import Menu
from fabricaPanes.Infraestructuras.PersistenciaProducto import PersistenciaProducto

if __name__== "__main__":
    saver = PersistenciaProducto()
    saver.connect()
    inventario= InventarioProductos()
    t=Tostada("vainilla","integral",2500,"lote-03") #sabor(vainilla), tipo(integral/normal), precio, lote
    p=Pan("Normal","Sal",1000,"lote-06") #tipo(integral/normal), gusto(dulce/salada), precio, lote
    g=Galleta("vainilla","cafe",900,"lote-03") #relleno(vainilla, chocolate), color(cafe, rojo), precio, lote
    d=Dulce("rollos","chocolate",800,"lote-13") #tipo(rollos, dona), sabor(vainilla, chocolate), precio, lote
    h=Hojaldre("vainilla","corazones",1800,"lote-53") #sabor(chocolate, vainilla), forma(corazones, chicharrones), precio, lote
    saver.guardar_producto(t)
    saver.guardar_producto(p)
    saver.guardar_producto(g)
    saver.guardar_producto(d)
    saver.guardar_producto(h)
    saver.save_json(t)
    saver.save_json(p)
    saver.save_json(g)
    saver.save_json(d)
    saver.save_json(h)
    for file in os.listdir("./Files"):
        if '.json' in file:
            inventario.agregar_Producto(saver.load_json(file))

    print(inventario.productos)

    menu = Menu()
    menu.buscar_producto()