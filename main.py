from report.api.busca_api import busca_usuario
from report.gerador.gerador_arquivo_txt import gerador_report

def gera_relatio_usuario(id_usuario: int):
    user_data = busca_usuario(id_usuario)
    gerador_report(user_data)

if __name__ == "__main__":
    gera_relatio_usuario(5)