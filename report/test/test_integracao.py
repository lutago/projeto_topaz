import pytest
import subprocess
import time
import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.busca_api import busca_usuario
from gerador.gerador_arquivo_txt import gerador_report

# Iniciar a aplicação backend como fixture
@pytest.fixture(scope="module", autouse=True)
def start_backend_app():
    # Comando para iniciar a aplicação backend (exemplo para FastAPI com uvicorn)
    cmd = ["uvicorn", "app.main_api:app_topaz", "--reload"]
    backend_process = subprocess.Popen(cmd)

    # Aguardar um momento para a aplicação iniciar
    time.sleep(2)

    # Verificar se a aplicação está ativa e acessível
    try:
        url = "http://127.0.0.1:8000/"
        response = requests.get(url)
        response.raise_for_status()
        yield
    except Exception as e:
        pytest.fail(f"Falha ao iniciar a aplicação backend: {e}")

    # Encerrar o processo da aplicação backend após os testes
    backend_process.terminate()
    backend_process.wait()

@pytest.fixture(scope="module")
def test_busca_usuario():
    response = busca_usuario(5)
    assert 'nome' in response
    assert isinstance(response['nome'], str)
    

# Teste de integração que depende da aplicação backend estar ativa
def test_integracao_geracao_relatorio(test_busca_usuario):
    try:
        gerador_report(test_busca_usuario['id'])
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Falha ao acessar a API: {e}")
