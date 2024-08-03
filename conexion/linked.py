import sqlite3

def establecer_conexion():
    # Establecer la conexión a la base de datos SQLite
    conn = sqlite3.connect('db\\users.db')
    return conn