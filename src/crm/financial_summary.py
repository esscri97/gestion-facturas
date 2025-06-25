from src.crm.db import connect

def get_users():
    """
    Recupera una lista básica de usuarios desde la base de datos.

    Acciones:
    - Consulta los usuarios y obtiene su id, nombre, apellidos y email.
    - Cierra la conexión a la base de datos.

    Retorna:
    - lista de tuplas con la información básica de cada usuario (id_usuario, nombre, apellidos, email).
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id_usuario, nombre, apellidos, email FROM usuarios")
    users = cursor.fetchall()

    conn.close()
    return users


def get_user_invoice_summary(user_id):
    """
    Obtiene el resumen financiero de facturas de un usuario específico.

    Parámetros:
    - user_id (int): Identificador único del usuario.

    Acciones:
    - Consulta las facturas asociadas a ese usuario.
    - Calcula el total de facturas, el monto total facturado, la suma de facturas pagadas y la suma de facturas pendientes.
    - Cierra la conexión a la base de datos.

    Retorna:
    - dict con las claves:
      * "total": número total de facturas.
      * "total_amount": suma total de todos los montos.
      * "paid": suma de montos de facturas pagadas.
      * "pending": suma de montos de facturas pendientes.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT monto, estado FROM facturas
        WHERE id_usuario = %s
    """, (user_id,))
    invoices = cursor.fetchall()

    conn.close()

    total = len(invoices)
    total_amount = sum(f[0] for f in invoices)
    paid = sum(f[0] for f in invoices if f[1] == "Pagada")
    pending = sum(f[0] for f in invoices if f[1] == "Pendiente")

    return {
        "total": total,
        "total_amount": total_amount,
        "paid": paid,
        "pending": pending
    }


def show_financial_summary():
    """
    Muestra en consola un resumen financiero detallado por usuario y un resumen general.

    Acciones:
    - Recupera todos los usuarios.
    - Por cada usuario, muestra:
        * Nombre completo y email
        * Total de facturas
        * Monto total facturado
        * Facturas pagadas y pendientes
    - Finalmente, muestra un resumen general con totales acumulados.
    """
    print("\n=== RESUMEN FINANCIERO ===")

    users = get_users()

    total_users = 0
    total_invoices = 0
    total_income = 0
    total_received = 0
    total_pending = 0

    for user in users:
        user_id, name, surname, email = user
        summary = get_user_invoice_summary(user_id)

        print(f"Usuario: {name} {surname} ({email})")
        print(f"- Total facturas: {summary['total']}")
        print(f"- Monto total: ${summary['total_amount']:.2f}")
        print(f"- Facturas pagadas: ${summary['paid']:.2f}")
        print(f"- Facturas pendientes: ${summary['pending']:.2f}\n")

        total_users += 1
        total_invoices += summary['total']
        total_income += summary['total_amount']
        total_received += summary['paid']
        total_pending += summary['pending']

    print("--- RESUMEN GENERAL ---")
    print(f"Total usuarios: {total_users}")
    print(f"Total facturas emitidas: {total_invoices}")
    print(f"Ingresos totales: ${total_income:.2f}")
    print(f"Ingresos recibidos: ${total_received:.2f}")
    print(f"Ingresos pendientes: ${total_pending:.2f}")
