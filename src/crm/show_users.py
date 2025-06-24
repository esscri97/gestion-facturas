from src.crm.db import connect

def show_users():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cont = 0
    if usuarios:
        print("\n--- LISTA DE USUARIOS ---")
        for usuario in usuarios:
            print(f"ID: USR00{usuario[0]}")
            print(f"Nombre: {usuario[1]} {usuario[2]}")
            print(f"Email: {usuario[3]}")
            print(f"Teléfono: {usuario[4] if usuario[4] else 'No especificado'}")
            print(f"Fecha de registro: {usuario[6]}\n")
            cont += 1
        print(f'Total de usuarios registrados: {cont}')
    else:
        print("No se han encontrado usuarios.")
    
    conn.close()
