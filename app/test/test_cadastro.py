import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_api import app_topaz

@pytest.fixture(scope="module")
def client():
    with TestClient(app_topaz) as c:
        yield c

def test_cadastro_usuario(client):
    response = client.post(
        "/cadastro/usuario",
        json={"nome": "Teste", "itens": [{"descricao": "Item Teste"}]}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Teste"
    assert len(data["itens"]) == 1
    assert data["itens"][0]["descricao"] == "Item Teste"

def test_cadastro_itens(client):
    response = client.post(
        "/cadastro/usuario",
        json={"nome": "Teste 2", "itens": [{"descricao": ""}]}
    )
    assert response.status_code == 201
    usuario_id = response.json()["id"]

    response = client.post(
        f"/cadastro/usuario/{usuario_id}/itens",
        json={"itens": [{"descricao": "Item Teste 2"}]}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["usuario_id"] == usuario_id
    assert len(data["itens"]) == 1
    assert data["itens"][0]["descricao"] == "Item Teste 2"