from src.crm.search_user import search_user_email, search_user_name
from src.crm.add_user import add_user

def test_buscar_usuario_no_existente():
    usuario = search_user_email("noexiste@email.com")
    assert usuario is None
    
def test_search_user_by_partial_name():
    add_user("Carlos", "Rodríguez", "carlos.r@example.com")
    add_user("Carlota", "Gómez", "carlota.g@example.com")

    resultados = search_user_name("Carl")

    emails = [u[3] for u in resultados]
    assert "carlos.r@example.com" in emails
    assert "carlota.g@example.com" in emails
    assert len(resultados) >= 2
