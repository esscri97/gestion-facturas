from src.crm.db import connect

def search_user_email(email):
    """
    Busca un usuario por email exacto en la base de datos.

    Parámetros:
    - email (str): Dirección de correo electrónico del usuario a buscar.

    Retorna:
    - Una tupla con los datos del usuario si se encuentra, o None si no existe.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    conn.close()
    return usuario


def search_user_name(nombre):
    """
    Busca uno o más usuarios cuyo nombre contenga el texto dado.

    Parámetros:
    - nombre (str): Texto parcial o completo del nombre a buscar.

    Retorna:
    - Una lista de tuplas con los usuarios encontrados (puede estar vacía).
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE ?", (f"%{nombre}%",))
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios


def show_user(usuario):
    """
    Muestra en consola los datos de un usuario formateados.

    Parámetros:
    - usuario (tuple): Registro del usuario recuperado desde la base de datos.

    Comportamiento:
    - Si el usuario existe, muestra sus datos. Si no, informa que no se encontró.
    """
    if usuario:
        print("\n--- USUARIO ENCONTRADO ---")
        print(f"ID: USR00{usuario[0]}")
        print(f"Nombre: {usuario[1]} {usuario[2]}")
        print(f"Email: {usuario[3]}")
        print(f"Teléfono: {usuario[4] if usuario[4] else 'No especificado'}")
        print(f"Dirección: {usuario[5] if usuario[5] else 'No especificada'}")
        print(f"Fecha de registro: {usuario[6]}")
    else:
        print("Usuario no encontrado.")


def search_user_menu():
    """
    Muestra un menú en consola para buscar usuarios por email o nombre.

    Flujo:
    - Permite buscar por email exacto o por nombre parcial.
    - Muestra los datos encontrados (uno o varios usuarios).
    - Maneja opciones no válidas.

    Entrada del usuario:
    - 1: Buscar por email.
    - 2: Buscar por nombre.
    """
    print("\n=== BUSCAR USUARIO ===")
    print("1. Buscar por email")
    print("2. Buscar por nombre")
    opcion = input("Seleccione método de búsqueda: ")

    if opcion == "1":
        email = input("Ingrese email: ")
        usuario = search_user_email(email)
        show_user(usuario)

    elif opcion == "2":
        nombre = input("Ingrese nombre: ")
        usuarios = search_user_name(nombre)
        if usuarios:
            print(f"\nSe encontraron {len(usuarios)} usuario(s):")
            for usuario in usuarios:
                show_user(usuario)
                print("-" * 40)
        else:
            print("No se encontraron usuarios con ese nombre.")

    else:
        print("Opción no válida.")
