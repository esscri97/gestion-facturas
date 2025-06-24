from src.crm.db import connect

def get_invoices_by_email(email):
    """
    Recupera todas las facturas asociadas al usuario identificado por su email.

    Parámetros:
    email (str): El correo electrónico del usuario cuyas facturas se desean obtener.

    Retorna:
    list: Una lista de tuplas con los datos de las facturas (id, fecha de emisión, descripción, monto, estado, nombre, apellidos).
          Retorna una lista vacía en caso de error o si no se encuentran facturas.
    """
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT f.id_factura, f.fecha_emision, f.descripcion, f.monto, f.estado, u.nombre, u.apellidos
            FROM facturas f
            JOIN usuarios u ON u.id_usuario = f.id_usuario
            WHERE u.email = ?
            ORDER BY f.fecha_emision
        """, (email,))

        facturas = cursor.fetchall()
        return facturas
    except Exception as e:
        print(f"Error al recuperar facturas: {e}")
        return []
    finally:
        conn.close()


def show_user_invoices():
    """
    Solicita al usuario un email, recupera las facturas asociadas y muestra por consola
    un resumen detallado incluyendo número, fecha, descripción, monto, estado, total de facturas,
    monto total facturado y monto pendiente.
    """
    print("\n=== FACTURAS POR USUARIO ===")
    email = input("Ingrese email del usuario: ").strip()

    facturas = get_invoices_by_email(email)

    if not facturas:
        print("No se encontraron facturas para ese usuario.")
        return

    full_name = f"{facturas[0][5]} {facturas[0][6]}"
    print(f"\n--- FACTURAS DE {full_name} ---\n")

    total_count = 0
    total_amount = 0
    pendiente = 0

    for i, factura in enumerate(facturas, start=1):
        print(f"Factura #{i}:")
        print(f"Número: FAC00{factura[0]}")
        print(f"Fecha: {factura[1]}")
        print(f"Descripción: {factura[2]}")
        print(f"Monto: ${factura[3]}")
        print(f"Estado: {factura[4]}\n")

        monto = factura[3]
        estado = factura[4]
        total_count += 1
        total_amount += monto
        if estado == "Pendiente":
            pendiente += monto

    print(f"Total de facturas: {total_count}")
    print(f"Monto total facturado: ${total_amount}")
    print(f"Monto pendiente: ${pendiente}")
