from src.crm.db import connect

def search_user_email(email):
    """
    Busca un usuario en la base de datos por su email.

    Parámetros:
    email (str): El correo electrónico del usuario a buscar.

    Retorna:
    tuple o None: Una tupla con los datos del usuario si se encuentra, 
                  o None si no existe ningún usuario con ese email.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    conn.close()
    return usuario


def search_user_name(nombre):
    """
    Busca usuarios en la base de datos cuyo nombre contenga la cadena dada.

    Parámetros:
    nombre (str): La cadena para buscar en el nombre del usuario (búsqueda parcial).

    Retorna:
    list: Una lista de tuplas con los datos de los usuarios que coincidan, 
          o una lista vacía si no hay coincidencias.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE ?", (f"%{nombre}%",))
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios


def show_user(usuario):
    """
    Muestra por consola los datos de un usuario.

    Parámetros:
    usuario (tuple o None): Los datos del usuario en forma de tupla, o None si no se encontró.
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
