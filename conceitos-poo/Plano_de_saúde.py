# Programa de cálculo de valor de plano de saúde
# Desenvolvido por: Karimy Carvalho Alves

# Mensagem de boas-vindas com nome e sobrenome
print('Bem-vindo ao sistema de planos de saúde!')
print('Você está sendo atendido por: Karimy')
print('-' * 50)

# Entrada de dados do usuário
valorBase = float(input('Digite o valor base do plano: R$ '))
idade = int(input('Digite a idade do cliente: '))

# Estruturas condicionais if, elif e else para aplicar as regras
if idade >= 0 and idade < 19:
    porcentagem = 100
elif idade >= 19 and idade < 29:
    porcentagem = 150
elif idade >= 29 and idade < 39:
    porcentagem = 225
elif idade >= 39 and idade < 49:
    porcentagem = 240
elif idade >= 49 and idade < 59:
    porcentagem = 350
else:  # idade maior ou igual a 59
    porcentagem = 600

# Cálculo do valor mensal
valorMensal = valorBase * (porcentagem / 100)

# Saída de dados
print('-' * 50)
print(f'Idade do cliente: {idade} anos')
print(f'Valor base informado: R$ {valorBase:.2f}')
print(f'Porcentagem aplicada: {porcentagem}%')
print(f'Valor mensal do plano: R$ {valorMensal:.2f}')
