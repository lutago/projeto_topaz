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

def test_excluir_usuario(client):
    response = client.post(
        "/cadastro/usuario",
        json={"nome": "Teste", "itens": [{"descricao": "Item Teste"}]}
    )
    assert response.status_code == 201
    data = response.json()
    id_usuario = data["id"]
    response = client.delete(
        f"/exluir/usuario/{id_usuario}"
    )
    assert response.status_code == 204
       
def test_excluir_tarefa_do_usuario(client):
    response = client.post(
        "/cadastro/usuario",
        json={"nome": "Teste", "itens": [{"descricao": "Item Teste"}]}
    )
    assert response.status_code == 201
    data = response.json()
    id_usuario = data["id"]
    id_tarefa = data["itens"][0]["id"]
    response = client.delete(
        f"/exluir/itens/{id_tarefa}/usuario/{id_usuario}"
    )
    assert response.status_code == 204