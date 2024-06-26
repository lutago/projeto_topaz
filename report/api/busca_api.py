import requests

def busca_usuario(user_id):
    url = f"http://127.0.0.1:8000/busca/usuarios/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()