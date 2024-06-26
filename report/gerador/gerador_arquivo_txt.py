def gerador_report(user_data):
    nome_usuario = user_data['nome']
    tarefas = user_data['itens']

    arquivo_report = f"{nome_usuario}.txt"
    with open(arquivo_report, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"Nome do usuário: {user_data['nome']}\n\n")
        
        for item in tarefas:
            arquivo.write(f"ID da tarefas: {item['id']}\n")
            arquivo.write(f"Data de criação tarefas: {item['data_criacao']}\n")
            arquivo.write(f"Descrição da tarefa:{item['descricao']}\n")
            arquivo.write(f"---------------------------------------\n")

    print(f"Relatório gerado: {arquivo_report}")