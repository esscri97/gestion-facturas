from src.crm.add_user import add_user
from src.crm.db import connect
from src.crm.financial_summary import get_users, get_user_invoice_summary

def test_get_users_and_summary():
    # Crear usuario
    email = "summary.test@example.com"
    add_user("Resumen", "Tester", email)

    # Obtener ID del usuario creado
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario FROM usuarios WHERE email = ?", (email,))
    user_id = cursor.fetchone()[0]

    # Crear facturas
    cursor.execute("""
        INSERT INTO facturas (id_usuario, descripcion, monto, estado)
        VALUES (?, ?, ?, ?)
    """, (user_id, "Auditoría mensual", 600, "Pagada"))

    cursor.execute("""
        INSERT INTO facturas (id_usuario, descripcion, monto, estado)
        VALUES (?, ?, ?, ?)
    """, (user_id, "Asesoría legal", 400, "Pendiente"))

    conn.commit()
    conn.close()

    # Comprobar que el usuario está en la lista de usuarios
    usuarios = get_users()
    correos = [u[3] for u in usuarios]
    assert email in correos

    # Verificar resumen financiero correcto
    resumen = get_user_invoice_summary(user_id)
    assert resumen["total"] == 2
    assert resumen["total_amount"] == 1000
    assert resumen["paid"] == 600
    assert resumen["pending"] == 400
