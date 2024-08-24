

#Lista para armazenar as campanhas
campanhas = []

#funcao para criar/cadastrar uma campanha
#informar os parametros de nome,descriçao,datainicio,datafim 
#(TODAS EM STRINGS)
def criar_campanha(nome, descricao, data_inicio, data_fim):
    """Cria uma nova campanha e a adiciona à lista de campanhas."""
    campanha = {
        'nome': nome,
        'descricao': descricao,
        'data_inicio': data_inicio,
        'data_fim': data_fim
    }
    campanhas.append(campanha)
    print(f"Campanha '{nome}' criada com sucesso!")

#funcao pra listar todas as campanhas e suas respectivas informacoes
#cadastradas
def listar_campanhas():
    """Lista todas as campanhas armazenadas."""
    if not campanhas:
        print("Nenhuma campanha cadastrada.")
    else:
        for i, campanha in enumerate(campanhas, start=1):
            print(f"Campanha {i}:")
            print(f"  Nome: {campanha['nome']}")
            print(f"  Descrição: {campanha['descricao']}")
            print(f"  Data de Início: {campanha['data_inicio']}")
            print(f"  Data de Fim: {campanha['data_fim']}\n")

#funcao para atualizar informacoes da campanha, pelo nome
#caso queira alterar apenas uma informação, basta seguir o exemplo:
# atualizar_campanha("nome_camapnha",novo_nome="novo_nome_campanha")
#nao passando os demais parametros, as informações seguem as mesmas
def atualizar_campanha(nome_antigo, novo_nome=None, nova_descricao=None, nova_data_inicio=None, nova_data_fim=None):
    """Atualiza uma campanha existente."""
    for campanha in campanhas:
        if campanha['nome'] == nome_antigo:
            if novo_nome:
                campanha['nome'] = novo_nome
            if nova_descricao:
                campanha['descricao'] = nova_descricao
            if nova_data_inicio:
                campanha['data_inicio'] = nova_data_inicio
            if nova_data_fim:
                campanha['data_fim'] = nova_data_fim
            print(f"Campanha '{nome_antigo}' atualizada com sucesso!")
            return
    print(f"Campanha '{nome_antigo}' não encontrada.")

#funcao remover campanha cadastrada pelo nome
def remover_campanha(nome):
    """Remove uma campanha pelo nome."""
    global campanhas
    campanhas = [campanha for campanha in campanhas if campanha['nome'] != nome]
    print(f"Campanha '{nome}' removida com sucesso!")

# teste como usar:
if __name__ == "__main__":
    criar_campanha("Campanha de Verão", "Promoções de verão para novos clientes.", "2024-06-01", "2024-08-31")
    listar_campanhas()
    atualizar_campanha("Campanha de Verão", nova_descricao="Promoções incríveis para a estação mais quente do ano!")
    listar_campanhas()
    remover_campanha("Campanha de Verão")
    listar_campanhas()
