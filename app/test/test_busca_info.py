import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main_api import app_topaz

@pytest.fixture(scope="module", name='client')
def client():
    with TestClient(app_topaz) as c:
        yield c

def test_busca_usuario(client):
    response = client.get("/busca/usuarios")
    assert response.status_code == 200
    data = response.json()
    assert data[4]["nome"] == "Eliane"
    assert len(data[4]["itens"]) == 1
    assert data[4]["itens"][0]["descricao"] == "Arrumar"

def test_busca_usuario_por_id(client):
    response = client.get(f"/busca/usuarios/5")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Osvaldo"
    assert len(data["itens"]) == 2
    assert data["itens"][1]["descricao"] == "programar"