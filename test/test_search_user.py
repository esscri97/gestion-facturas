from src.crm.search_user import search_user_email

def test_buscar_usuario_no_existente():
    usuario = search_user_email("noexiste@email.com")
    assert usuario is None
