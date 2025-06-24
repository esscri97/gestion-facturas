from src.crm.db import connect

ESTADOS = {
    "1": "Pendiente",
    "2": "Pagada",
    "3": "Cancelada"
}

def create_invoice():
    print("\n=== CREAR FACTURA ===")
    conn = connect()
    cursor = conn.cursor()

    while True:
        email = input("Ingrese email del usuario (o pulse 7 para salir): ").strip()

        if email == "7":
            conn.close()
            return
        # Verificamos si el usuario existe
        cursor.execute("SELECT id_usuario, nombre, apellidos FROM usuarios WHERE email = ?", (email,))
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
            VALUES (?, ?, ?, ?)
        """, (id_usuario, descripcion, monto, estado))
        conn.commit()

        factura_id = cursor.lastrowid
        cursor.execute("SELECT fecha_emision FROM facturas WHERE id_factura = ?", (factura_id,))
        fecha_emision = cursor.fetchone()[0]

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
