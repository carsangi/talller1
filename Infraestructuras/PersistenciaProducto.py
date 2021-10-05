import pickle
import sqlite3
from builtins import type, object

import jsonpickle

from fabricaPanes.Dominio.Pan import Pan
from fabricaPanes.Dominio.Galleta import Galleta
from fabricaPanes.Dominio.Hojaldre import Hojaldre
from fabricaPanes.Dominio.Dulce import Dulce
from fabricaPanes.Dominio.Tostada import Tostada


class PersistenciaProducto():

    def connect(self):
        self.con = sqlite3.connect("fabrica_de_panes.db")
        self.__crear_tabla_Tostada()
        self.__crear_tabla_Pan()
        self.__crear_tabla_Galleta()
        self.__crear_tabla_Dulce()
        self.__crear_tabla_Hojaldre()


    def __crear_tabla_Tostada(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE TOSTADAS(id text primary key, sabor txt ," \
                    " tipo txt,precio int,lote txt) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_Pan(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PANES(id text primary key, tipo txt ," \
                    " gusto txt,precio int,lote txt) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_Galleta(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE GALLETAS(id text primary key, relleno txt ," \
                    " color txt,precio int,lote txt) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_Dulce(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE DULCES(id text primary key, tipo txt ," \
                    " sabor txt,precio int,lote txt) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def __crear_tabla_Hojaldre(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE HOJALDRES(id text primary key, sabor txt ," \
                    " forma txt,precio int,lote txt) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass


    def guardar_producto(self,producto):
        cursor = self.con.cursor()
        if isinstance(producto,Tostada):
            query = "insert into TOSTADAS(id, sabor, tipo ,precio ,lote) " \
                "values("f" ?,?,?,?,?)"
            cursor.execute(query,(str(producto.id),producto.sabor,producto.tipo,
                                  producto.precio, producto.lote))
        elif isinstance(producto,Pan):
            query = "insert into PANES(id, tipo, gusto ,precio ,lote) " \
                    "values("f" ?,?,?,?,?)"
            cursor.execute(query, (str(producto.id), producto.tipo, producto.gusto,
                                   producto.precio, producto.lote))
        elif isinstance(producto,Galleta):
            query = "insert into GALLETAS(id, relleno, color ,precio ,lote) " \
                    "values("f" ?,?,?,?,?)"
            cursor.execute(query, (str(producto.id), producto.relleno, producto.color,
                                   producto.precio, producto.lote))
        elif isinstance(producto,Dulce):
            query = "insert into DULCES(id, tipo, sabor ,precio ,lote) " \
                    "values("f" ?,?,?,?,?)"
            cursor.execute(query, (str(producto.id), producto.tipo, producto.sabor,
                                   producto.precio, producto.lote))
        elif isinstance(producto,Hojaldre):
            query = "insert into HOJALDRES(id, sabor, forma ,precio ,lote) " \
                    "values("f" ?,?,?,?,?)"
            cursor.execute(query, (str(producto.id), producto.sabor, producto.forma,
                                   producto.precio, producto.lote))
        else:
            print("no guardo")
        self.con.commit()

    @classmethod
    def save_json(cls, producto):
        text_open = open("Files/" + str(producto.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(producto)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("Files/"+file_name, mode='r')
        json_gui = text_open.readline()
        producto = jsonpickle.decode(json_gui)
        text_open.close()
        return producto