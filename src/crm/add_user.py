import re
from .db import connect

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def add_user(nombre, apellidos, email, telefono=None, direccion=None):
    """
    Registra un nuevo usuario en la base de datos.

    Parámetros:
    - nombre (str): Nombre del usuario.
    - apellidos (str): Apellidos del usuario.
    - email (str): Dirección de correo electrónico (debe ser válida y única).
    - telefono (str, opcional): Número de teléfono.
    - direccion (str, opcional): Dirección postal.

    Validaciones:
    - El email debe tener un formato válido.
    - Se captura cualquier excepción generada durante la inserción (por ejemplo, email duplicado).

    Acciones:
    - Inserta el usuario en la base de datos.
    - Recupera y muestra la fecha de registro asignada automáticamente.
    """
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
