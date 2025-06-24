from src.crm.db import start_db
from src.crm.add_user import add_user
from src.crm.search_user import search_user_menu

def add_interactive_user():
    print("=== REGISTRO DE NUEVO USUARIO ===")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    email = input("Email: ")
    telefono = input("Teléfono (opcional): ") or None
    direccion = input("Dirección (opcional): ") or None

    add_user(nombre, apellidos, email, telefono, direccion)

def main():
    start_db()

    while True:
        print("""
=== SISTEMA CRM ===
1. Registrar nuevo usuario
2. Buscar usuario
3. Crear factura para usuario
4. Mostrar todos los usuarios
5. Mostrar facturas de un usuario
6. Resumen financiero por usuario
7. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            add_interactive_user()
        elif opcion == "2":
            search_user_menu()
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
