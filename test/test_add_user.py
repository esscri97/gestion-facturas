import pytest
from src.crm.add_user import add_user

def test_add_user_invalid_email(capfd):
    add_user("Juan", "Pérez", "juanemail.com")  # Email sin @ ni dominio
    out, err = capfd.readouterr()
    assert "Email no tiene un formato válido." in out
