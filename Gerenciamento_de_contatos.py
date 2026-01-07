# Sistema de gerenciamento de Contatos Comerciais
# Desenvolvido por: Karimy Carvalho Alves

# Mensagem de boas-vindas
print('Bem-vindo ao sistema de gerenciamento de Contatos Comerciais Karimy Alves!')

# Lista onde os contatos serão armazenados
lista_contatos = []

# Variável que armazena o id único de cada contato (com meu RU)
id_global = 5562007

# Cadastrar um contato
def cadastrar_contato(id):
    print('---------------- MENU CADASTRAR CONTATO ----------------')
    print(f'Id do Contato: {id}')
    nome = input('Nome do Contato: ')
    atividade = input('Atividade do contato: ')
    telefone = input('Telefone do contato: ')

    contato = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }

    lista_contatos.append(contato)
    print()

# Consultar contatos
def consultar_contatos():
    while True:
        print('---------------- MENU CONSULTAR CONTATOS ----------------')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos os Contatos')
        print('2 - Consultar Contato por id')
        print('3 - Consultar Contato(s) por Atividade')
        print('4 - Retornar')
        opcao = input('>> ')

        if opcao == '1':
            print()
            for contato in lista_contatos:
                print(f'id: {contato['id']}')
                print(f'nome: {contato['nome']}')
                print(f'atividade: {contato['atividade']}')
                print(f'telefone: {contato['telefone']}')
                print()

        elif opcao == '2':
            id_busca = input('Digite o id do contato: ')
            print()
            encontrado = False
            for contato in lista_contatos:
                if str(contato['id']) == id_busca:
                    print(f'id: {contato['id']}')
                    print(f'nome: {contato['nome']}')
                    print(f'atividade: {contato['atividade']}')
                    print(f'telefone: {contato['telefone']}')
                    print()
                    encontrado = True
                    break
            if not encontrado:
                print('Contato não encontrado.\n')

        elif opcao == '3':
            atividade_busca = input('Digite a Atividade do(s) Contato(s): ')
            print()
            encontrados = [c for c in lista_contatos if c['atividade'].lower() == atividade_busca.lower()]
            if encontrados:
                for c in encontrados:
                    print(f'id: {c['id']}')
                    print(f'nome: {c['nome']}')
                    print(f'atividade: {c['atividade']}')
                    print(f'telefone: {c['telefone']}')
                    print()
            else:
                print('Nenhum contato encontrado com essa atividade.\n')

        elif opcao == '4':
            print()
            return

        else:
            print('Opção inválida. Tente novamente.\n')

# Remover contato por ID
def remover_contato():
    id_remover = input('Digite o id do contato a ser removido: ')
    for contato in lista_contatos:
        if str(contato['id']) == id_remover:
            lista_contatos.remove(contato)
            print('Contato removido com sucesso!\n')
            return
    print('Contato não encontrado.\n')

# Estrutura do código
while True:
    print('---------------- MENU PRINCIPAL ----------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Contato')
    print('2 - Consultar Contato(s)')
    print('3 - Remover Contato')
    print('4 - Sair')
    opcao = input('>> ')

    if opcao == '1':
        cadastrar_contato(id_global)
        id_global += 1

    elif opcao == '2':
        consultar_contatos()

    elif opcao == '3':
        remover_contato()

    elif opcao == '4':
        print('\nEncerrando o programa. Até logo!')
        break

    else:
        print('Opção inválida. Tente novamente.\n')