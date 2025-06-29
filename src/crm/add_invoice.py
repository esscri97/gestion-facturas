from src.crm.db import connect

ESTADOS = {
    "1": "Pendiente",
    "2": "Pagada",
    "3": "Cancelada"
}

def create_invoice():
    """
    Crea una factura asociada a un usuario existente, solicitando los datos por consola.
    
    Validaciones:
    - El email debe existir en la base de datos.
    - La descripción no puede estar vacía.
    - El monto debe ser un número mayor a cero.
    - El estado debe ser una de las opciones válidas.

    Conexión a base de datos:
    - La conexión se mantiene abierta mientras el usuario introduce un email válido.
    - Se cierra correctamente al finalizar el proceso o en caso de error.
    """
    print("\n=== CREAR FACTURA ===")
    conn = connect()
    cursor = conn.cursor()

    while True:
        email = input("Ingrese email del usuario (o pulse 7 para salir): ").strip()

        if email == "7":
            conn.close()
            return
        cursor.execute("SELECT id_usuario, nombre, apellidos FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()

        if usuario:
            break
        else:
            print("Usuario no encontrado.")

    id_usuario, nombre, apellidos = usuario
    print(f"Usuario encontrado: {nombre} {apellidos}")

    descripcion = input("Ingrese descripción del servicio/producto: ").strip()
    if not descripcion:
        print("La descripción no puede estar vacía.")
        conn.close()
        return

    try:
        monto = float(input("Ingrese monto total: "))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            conn.close()
            return
    except ValueError:
        print("El monto debe ser un número.")
        conn.close()
        return

    print("Seleccione estado:")
    print("1. Pendiente")
    print("2. Pagada")
    print("3. Cancelada")
    estado_input = input("Estado: ").strip()
    estado = ESTADOS.get(estado_input)

    if not estado:
        print("Estado no válido.")
        conn.close()
        return

    try:
        cursor.execute("""
            INSERT INTO facturas (id_usuario, descripcion, monto, estado)
            VALUES (%s, %s, %s, %s)
            RETURNING id_factura, fecha_emision
        """, (id_usuario, descripcion, monto, estado))
        result = cursor.fetchone()
        conn.commit()

        if result:
            factura_id, fecha_emision = result
        else:
            factura_id, fecha_emision = "No disponible", "No disponible"

        print(f"""
Factura creada exitosamente!
Número de factura: FAC00{factura_id}
Fecha de emisión: {fecha_emision}
Cliente: {nombre} {apellidos}
Descripción: {descripcion}
Monto: ${monto}
Estado: {estado}
        """)
    except Exception as e:
        print(f"Error al crear factura: {e}")
    finally:
        conn.close()
