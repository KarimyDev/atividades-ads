# Programa de pedidos de pizza
# Desenvolvido por: Karimy Carvalho Alves

# Mensagem de boas-vindas + Menu
print('Bem-vindo(a) ao sistema de pedidos da Pizzaria!')
print('Você está sendo atendido por: Karimy')
print('-' * 60)
print('MENU DE SABORES E TAMANHOS')
print('PS = Pizza Salgada | PD = Pizza Doce')
print('Tamanhos disponíveis: P (Pequena), M (Média), G (Grande)')
print("Valores:")
print('  P: PS = R$30, PD = R$34')
print('  M: PS = R$45, PD = R$48')
print('  G: PS = R$60, PD = R$66')
print('-' * 60)

# acumulador para somar os valores do pedido
total_pedido = 0

# estrutura de repetição (while)
while True:
    # Input do sabor
    sabor = input('Digite o sabor (PS/PD): ').upper()
    if sabor not in ['PS', 'PD']:
        print('Sabor inválido. Tente novamente.')
        continue  # volta para pedir novamente

    # Input do tamanho
    tamanho = input('Digite o tamanho (P/M/G): ').upper()
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente.')
        continue  # volta para pedir novamente

    # Estrutura if/elif/else aninhada para determinar o preço
    if sabor == 'PS':  # Pizza Salgada
        if tamanho == 'P':
            preco = 30
        elif tamanho == 'M':
            preco = 45
        else:  # tamanho G
            preco = 60
    else:  # Pizza Doce
        if tamanho == 'P':
            preco = 34
        elif tamanho == 'M':
            preco = 48
        else:  # tamanho G
            preco = 66

    # Soma no acumulador
    total_pedido += preco
    print(f'Item adicionado: {sabor} {tamanho} - R$ {preco:.2f}')

    # Perguntar se deseja pedir mais alguma coisa
    mais = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
    if mais != 'S':
        break  # encerra o loop

# Saída final do programa
print('-' * 60)
print(f'Valor total do pedido: R$ {total_pedido:.2f}')
print('Seu pedido será entregue em 40min, até o próximo pedido!')
