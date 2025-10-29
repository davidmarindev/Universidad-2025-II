import sqlite3

DB_URL = "./northwind.db"

def crear_conn():
    try:
      conn = sqlite3.connect(DB_URL)

      print("Conexión exitosa")
      
      return conn

    except:
      print("Error")