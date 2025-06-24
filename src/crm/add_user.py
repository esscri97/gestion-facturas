import re
from .db import connect

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def add_user(nombre, apellidos, email, telefono=None, direccion=None):
    if not re.match(EMAIL_REGEX, email):
        print("Email no tiene un formato válido.")
        return

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO usuarios (nombre, apellidos, email, telefono, direccion)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, apellidos, email, telefono, direccion))
        conn.commit()

        id_usuario = cursor.lastrowid

        cursor.execute("SELECT fecha_registro FROM usuarios WHERE id_usuario = ?", (id_usuario,))
        fecha_registro = cursor.fetchone()[0]

        print(f"""
            Usuario registrado exitosamente!
            ID asignado: {id_usuario}
            Fecha de registro: {fecha_registro}
            """)
    except Exception as e:
        print(f"Error al agregar usuario: {e}")
    finally:
        conn.close()
