import sqlite3

DB_PATH = "crm.db"

def connect():
    return sqlite3.connect(DB_PATH)

def start_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(50) NOT NULL,
            apellidos VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            telefono VARCHAR(15),
            direccion VARCHAR(255),
            fecha_registro DATE DEFAULT (DATE('now'))
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facturas (
            id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            fecha_emision DATE DEFAULT (DATE('now')),
            descripcion VARCHAR(255) NOT NULL,
            monto REAL NOT NULL CHECK (monto > 0),
            estado VARCHAR(10) CHECK (estado IN ('Pendiente', 'Pagada', 'Cancelada')) NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
        );
    """)

    conn.commit()
    conn.close()
