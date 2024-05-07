import sqlite3 
from sqlite3 import Error


def crear_conexion(sql):    
        try:
                conn = sqlite3.connect("bdCripto.sqlite", timeout=100)
                cursor = conn.cursor()
                resultado = cursor.execute(sql)
                resultado = cursor.fetchone()
                conn.commit()
                return resultado
                  

        except sqlite3.IntegrityError as e:
                print(e)
                print("Codigo del error:", e.sqlite_errorcode)
                assert e.sqlite_errorcode == sqlite3.SQLITE_CONSTRAINT_UNIQUE
                print("Nombre del error:", e.sqlite_errorname)
                print("Clase de la excepcion: ", er.__class__)
                print('Error de SQLite: %s' % (' '.join(er.args)))
                print("falló la conexion")

        finally:
                if conn:
                        conn.close() 


def crear_conexion_lista(sql):    
        try:
                conn = sqlite3.connect("bdCripto.sqlite", timeout=100)
                cursor = conn.cursor()
                resultado = cursor.execute(sql)
                resultado = cursor.fetchall()
                conn.commit()
                return resultado
                  

        except sqlite3.IntegrityError as e:
                print(e)
                print("Codigo del error:", e.sqlite_errorcode)
                assert e.sqlite_errorcode == sqlite3.SQLITE_CONSTRAINT_UNIQUE
                print("Nombre del error:", e.sqlite_errorname)
                print("Clase de la excepcion: ", er.__class__)
                print('Error de SQLite: %s' % (' '.join(er.args)))
                print("falló la conexion")

        finally:
                if conn:
                        conn.close() 
