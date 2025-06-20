import sqlite3

DB_PATH = "crm.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def inicializar_db():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefono TEXT,
            direccion TEXT,
            fecha_registro DATE DEFAULT (DATE('now'))
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facturas (
            id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            fecha_emision DATE DEFAULT (DATE('now')),
            descripcion TEXT NOT NULL,
            monto REAL NOT NULL CHECK (monto > 0),
            estado TEXT CHECK (estado IN ('Pendiente', 'Pagada', 'Cancelada')) NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
        );
    """)

    conn.commit()
    conn.close()
