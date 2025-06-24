from src.crm.financial_summary import get_user_invoice_summary

def test_user_invoice_summary_sin_facturas():
    resumen = get_user_invoice_summary(9999)  # ID improbable
    assert resumen["total"] == 0
    assert resumen["total_amount"] == 0
    assert resumen["paid"] == 0
    assert resumen["pending"] == 0
