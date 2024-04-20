# Universo: Ilustrador Free Lancer
# Em entrevista com trabalhador da área (meu marido) surgiu a ideia de abordar esse universo para o projeto.
# O sistema conta com uma lista de comissões (nome do meio artístico para os "pedidos" de artes). No input, entram os
# dados de identificação dos clientes. O dado mais importante e de identificação única é o e-mail (uma vez que é comum
# dois clientes com o mesmo nome). Além disso, também são inputs o nome, a data em que a comissão foi solicitada,
# uma descrição curta do que é o pedido, quantidade de itens daquele pedido (é comum serem solicitadas mais que uma
# arte no pedido), o prazo de entrega com a data alvo e o status do pagamento (alguns pedidos ficam como "a pagar",
# porém a maioria já estão 50% pagos ou totalmente pagos). No dicionário também terá a informação de quantidade de
# itens pendentes, onde no início será igual ao número de itens total, mas poderá ser alterado na função de atualização.
# OBS: para a data da comissão, a princípio iria utilizar a função datetime.now() da biblioteca datetime porém, para
# podermos trabalhar com datas diferentes, irei deixar um campo como string
#
# Funcionalidade adicional: cotação de arte; após o input da quantidade de artes a ser solicitada e os dados de cada
# pedido, o sistema diz o valor médio do pedido, o desconto (se houver) e o valor com desconto. Além disso, é possível
# adicionar a cotação à lista de comissões.
# Dados do pedido: tipo (Rascunho, flat colors, arte final) e tamanho da arte (busto, meio corpo, corpo completo)
#
# Regra de negócio: desconto no valor da cotação baseado na quantidade de artes solicitadas
# Exemplo: 3 ou 4 artes: 5% off; 5 artes: 10% off; 5 artes de corpo completo: 15% off
#
# Interface: o sistema contará com uma interface simples no estilo de menu, com opções de 1 a 8 em que o usuário irá
# determinar a função a ser utilizada.


def mock_teste(comissoes):
    # Mock do dicionário para teste
    comissoes = {"pedrinho@gmail.com": {"nome": "Pedro", "data": "24/12/2024",
                                        "descricao": "1 gigante, 1 bruxa e 1 esqueleto corpos inteiros",
                                        "prazo": "16/04/2024", "quantidade_total": 3, "quantidade_pendente": 3,
                                        "status_pagamento": "50% PAGO"},
                 "marcos_antonio@hotmail.com": {"nome": "Marcos Antônio", "data": "25/01/2024",
                                                "descricao": "1 elfo, 1 orc, 2 bruxos, 1 mago, bustos",
                                                "prazo": "17/04/2024", "quantidade_total": 5,
                                                "quantidade_pendente": 2,
                                                "status_pagamento": "PAGO"},
                 "teste_zerado@hotmail.com": {"nome": "Zero", "data": "25/02/2024",
                                              "descricao": "3 magos corpos inteiros",
                                              "prazo": "25/04/2024", "quantidade_total": 3,
                                              "quantidade_pendente": 0,
                                              "status_pagamento": "50% PAGO"}}
    return comissoes


# Função para limpar o console no PyCharm na base da gambiarra mesmo, pois não achei como faz direito
# OBS: testei o import os e a função clear, mas não funcionou
def limpar_console():
    print("\n" * 15)


# Função para incluir a comissão na lista de comissões
def incluir_comissao(quantidade):
    nome = input("Informe o nome do cliente: ")
    email = input("Informe o e-mail do cliente: ")
    data = input("Informe a data da abertura da comissão (DD/MM/YY): ")
    descricao = input("Insira a descrição curta do pedido: ")
    prazo = input("Informe a data alvo do pedido: ")
    if quantidade != -1:
        quantidade_total = quantidade
    else:
        quantidade_total = int(input("Informe o total de itens: "))
    status_pagamento = input("Informe a situação do pagamento (A PAGAR/50% PAGO/PAGO): ")
    comissoes[email] = {"nome": nome, "data": data, "descricao": descricao, "prazo": prazo,
                        "quantidade_total": quantidade_total, "quantidade_pendente": quantidade_total,
                        "status_pagamento": status_pagamento}
    # Na inclusão, a quantidade de itens pendentes vai ser sempre a mesma da quantidade de itens total
    print(f"\nPedido do cliente {email} adicionado com sucesso!")


# Função para listar todas as comissões
def listar_comissoes():
    if comissoes:
        print("===Lista de comissões===")
        for i, (email, detalhes) in enumerate(comissoes.items(), start=1):
            print(f"Nome: {detalhes['nome']}")
            print(f"E-mail: {email}")
            print(f"Descrição: {detalhes['descricao']}")
            print(f"Data do pedido: {detalhes['data']}")
            print(f"Data Alvo/Prazo: {detalhes['prazo']}")
            print(f"Quantidade de itens do pedido: {detalhes['quantidade_total']}")
            print(f"Quantidade de itens pendentes: {detalhes['quantidade_pendente']}")
            print(f"Status do pagamento: {detalhes['status_pagamento']}")
            print("\n")
    else:
        print("Lista vazia.")


# Função para listar todas as comissões em aberto: as que ainda estão com algum item pendente
def listar_comissoes_abertas():
    if comissoes:
        print("===Lista de comissões abertas===")
        for i, (email, detalhes) in enumerate(comissoes.items(), start=1):
            if detalhes['quantidade_pendente'] > 0:
                print(f"Nome: {detalhes['nome']}")
                print(f"E-mail: {email}")
                print(f"Descrição: {detalhes['descricao']}")
                print(f"Data do pedido: {detalhes['data']}")
                print(f"Data Alvo/Prazo: {detalhes['prazo']}")
                print(f"Quantidade de itens do pedido: {detalhes['quantidade_total']}")
                print(f"Quantidade de itens pendentes: {detalhes['quantidade_pendente']}")
                print(f"Status do pagamento: {detalhes['status_pagamento']}")
                print("\n")
    else:
        print("Lista vazia.")


# Função para atualizar informação de quantidade de itens pendentes
def atualizar_comissao():
    if comissoes:
        email = input("Insira o e-mail do pedido a ser atualizado: ")
        if email in comissoes:
            detalhes = comissoes[email]
            print(f"Quantidade atual de itens pendentes: {detalhes['quantidade_pendente']}")
            nova_quantidade_pendentes = int(input("Digite a nova quantidade de itens pendentes: "))
            if nova_quantidade_pendentes < detalhes['quantidade_pendente']:
                detalhes['quantidade_pendente'] = nova_quantidade_pendentes
                print("Quantidade de itens pendentes atualizada")
            elif nova_quantidade_pendentes == nova_quantidade_pendentes:
                print("Quantidade de itens pendentes não foi alterada")
            else:
                print("Comando não permitido.")
            print("\n")
        else:
            print(f"Comissão não encontrada.")
    else:
        print("Lista vazia.")


# Função para buscar comissão específica
def buscar_comissao():
    if comissoes:
        email = input("Insira o e-mail do pedido a ser procurado: ")
        if email in comissoes:
            detalhes = comissoes[email]
            print(f"Nome: {detalhes['nome']}")
            print(f"E-mail: {email}")
            print(f"Descrição: {detalhes['descricao']}")
            print(f"Data do pedido: {detalhes['data']}")
            print(f"Data Alvo/Prazo: {detalhes['prazo']}")
            print(f"Quantidade de itens do pedido: {detalhes['quantidade_total']}")
            print(f"Quantidade de itens pendentes: {detalhes['quantidade_pendente']}")
            print(f"Status do pagamento: {detalhes['status_pagamento']}")
            print("\n")
        else:
            print(f"Comissão não encontrada.")
    else:
        print("Lista vazia.")


# Sistema de "trava" de menu para poder ler as comissões listadas e não printar o menu de novo sem o comando
def trava_menu():
    escolha = input(f"\nDigite qualquer coisa para continuar: ")


# Função para excluir comissão da lista
def cancelar_comissao():
    if comissoes:
        email = input("Insira o e-mail do pedido a ser atualizado: ")
        if email in comissoes:
            del comissoes[email]
            print(f"Comissão do cliente {email} excluída com sucesso!")
        else:
            print("Contato não encontrado na agenda.")
    else:
        print("Lista vazia.")


# Sistema de cotação de artes
# 3 ou 4 artes: 5% off; 5 artes: 10% off; 5 artes de corpo completo: 15% off
def cotacao_arte():
    # definição de variáveis
    total = 0
    qtd_completo = 0
    precos = {
        "rascunho": {"busto": 30.0, "meio": 40.0, "completo": 50.0},
        "flat": {"busto": 60.0, "meio": 70.0, "completo": 80.0},
        "final": {"busto": 50.0, "meio": 75.0, "completo": 100.0},
    }

    limpar_console()
    quantidade = int(input("Informe quantas artes serão feitas: "))
    while quantidade <= 0:
        print("Quantidade inválida. Digite um número maior que 0.")
        quantidade = int(input("Informe quantas artes serão feitas: "))
    for i in range(quantidade):
        print(f"\nArte número {i+1}: ")
        print("=== Tipos de arte ===")
        print("1. Rascunho")
        print("2. Flat colors")
        print("3. Arte final")
        tipo = int(input("Insira o tipo da arte (1 a 3): "))
        while tipo > 3:
            print("Tipo inválido. Digite um número de 1 a 3.")
            tipo = int(input("Insira o tipo da arte (1 a 3): "))
        print("=== Tamanhos de arte ===")
        print("1. Busto")
        print("2. Meio corpo")
        print("3. Corpo Completo")
        tamanho = int(input("Insira o tamanho de arte (1 a 3): "))
        while tamanho > 3:
            print("Tamanho inválido. Digite um número de 1 a 3.")
            tamanho = int(input("Insira o tamanho de arte (1 a 3): "))
        # tradução do número digitado para
        if tipo == 1:
            nome_tipo = "rascunho"
        elif tipo == 2:
            nome_tipo = "flat"
        else:
            nome_tipo = "final"
        if tamanho == 1:
            nome_tamanho = "busto"
        elif tamanho == 2:
            nome_tamanho = "meio"
        else:
            nome_tamanho = "completo"
        preco = precos[nome_tipo][nome_tamanho]
        total += preco
        if nome_tamanho == "completo":
            qtd_completo += 1
    if quantidade >= 5 & qtd_completo >= 5:
        desconto = 15
    elif quantidade >= 5:
        desconto = 10
    elif quantidade == 3 or quantidade == 4:
        desconto = 5
    else:
        desconto = 0

    total_com_desconto = total * (1 - desconto/100)

    print(f"\nO preço das {quantidade} comissões foi de R$ {total:.2f}")
    if desconto > 0:
        print(f"Você possui um desconto de {desconto}%.")
        print(f"O valor com desconto aplicado é R$ {total_com_desconto:.2f}")
    decisao = input("Deseja adicionar essa comissão à lista? (S/N): ")
    while decisao != "S" and decisao != "N":
        print("Formato inválido. Escolha S ou N.")
        decisao = input("Deseja adicionar essa comissão à lista? (S/N): ")
    if decisao == "S":
        incluir_comissao(quantidade)
    trava_menu()


comissoes = {}
# Mock de dados para teste: descomentar a linha abaixo em caso de teste com dicionário mockado
# comissoes = mock_teste(comissoes)

# Loop do menu
while True:
    print("\n=== Lista de comissões ===")
    print("1. Incluir comissão")
    print("2. Buscar comissão")
    print("3. Listar todas as comissões")
    print("4. Listar comissões em aberto")
    print("5. Atualizar informações de comissões")
    print("6. Cancelar comissão")
    print("7. Cotação de arte")
    print("8. Encerrar programa")
    print("\n")

    # Input da informação
    opcao = int(input("Escolha uma opção (número do item): "))
    # Limpar a tela antes de mostrar as demais opções ou ações
    limpar_console()

    if opcao == 1:  # 1. Incluir comissão
        decisao = "N"
        quantidade = -1
        incluir_comissao(quantidade)
    elif opcao == 2:  # 2. Buscar comissão
        buscar_comissao()
        trava_menu()
    elif opcao == 3:  # 3. Listar todas as comissões
        listar_comissoes()
        trava_menu()
    elif opcao == 4:  # 4. Listar comissões em aberto
        listar_comissoes_abertas()
        trava_menu()
    elif opcao == 5:  # 5. Atualizar informações de comissões
        atualizar_comissao()
        trava_menu()
    elif opcao == 6:  # 6. Cancelar comissão
        cancelar_comissao()
        trava_menu()
    elif opcao == 7:  # 7. Cotação de artes
        cotacao_arte()
    elif opcao == 8:  # 8. Encerrar o programa
        limpar_console()
        break
    else:  # Digitou opção inválida
        print("Opção inválida. Digite um número de 1 a 6")

    limpar_console()

listar_comissoes()
