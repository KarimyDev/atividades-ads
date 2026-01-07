# Sistema de Venda de Toras de Madeira
# Desenvolvido por: Karimy Carvalho Alves

# Mensagem de boas-vindas
print('Bem-vindo ao sistema de vendas da Empresa Karimy Lenhadora!')
print('-' * 60)

# Tabela de preços por tipo de madeira (valor por m³)
precos = {
    'PINHO': 150.40,
    'PEROBA': 170.20,
    'MOGNO': 190.90,
    'IPE': 202.10,
    'IMBUIA': 220.70
}

# Escolha do tipo de madeira
def escolha_tipo():
    while True:
        tipo = input('Digite o tipo de madeira (PINHO/PEROBA/MOGNO/IPE/IMBUIA): ').upper()
        if tipo in precos:
            return precos[tipo]  # retorna o valor do tipo escolhido
        else:
            print('Tipo inválido! Tente novamente.')

# Quantidade de toras + desconto
def qtd_toras():
    while True:
        try:
            qtd = int(input('Digite a quantidade de toras (em m³, máximo 2000 m³): '))
            if qtd > 2000:
                print('Quantidade não permitida! Máximo aceito é 2000 m³. Tente novamente.')
                continue  # volta para perguntar de novo
            elif qtd < 0:
                print('Quantidade inválida, não pode ser negativa.')
                continue

            # Definição do desconto
            if qtd < 100:
                desconto = 0
            elif qtd < 500:
                desconto = 0.04
            elif qtd < 1000:
                desconto = 0.09
            else:  # entre 1000 e 2000
                desconto = 0.16

            return qtd, desconto
        except ValueError:
            print('Valor inválido! Digite apenas números.')

# Transporte
def transporte():
    while True:
        opcao = input('Escolha transporte (1-Rodoviário | 2-Ferroviário | 3-Hidroviário): ')
        if opcao == '1':
            return 1000
        elif opcao == '2':
            return 2000
        elif opcao == '3':
            return 2500
        else:
            print('Opção inválida, tente novamente.')

# Total à pagar (main)
def main():
    try:
        valor_madeira = escolha_tipo()
        qtd, desconto = qtd_toras()
        if qtd is None:  # caso ultrapasse limite de 2000
            return

        valor_transporte = transporte()

        # Valor final
        total = ((valor_madeira * qtd) * (1 - desconto)) + valor_transporte

        print('-' * 60)
        print(f'Quantidade: {qtd} m³')
        print(f'Valor unitário: R$ {valor_madeira:.2f}')
        print(f'Desconto aplicado: {desconto*100:.0f}%')
        print(f'Transporte: R$ {valor_transporte:.2f}')
        print(f'TOTAL A PAGAR: R$ {total:.2f}')
        print('-' * 60)

    except Exception as e:
        print('Erro inesperado:', e)

main()
