from src.crm.db import connect

def get_users():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id_usuario, nombre, apellidos, email FROM usuarios")
    users = cursor.fetchall()

    conn.close()
    return users


def get_user_invoice_summary(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT monto, estado FROM facturas
        WHERE id_usuario = ?
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
