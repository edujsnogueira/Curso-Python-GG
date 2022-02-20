# Exercício 071:

'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o
valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: considere como disponíveis as cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''

print('-=-' * 10)
print('Caixa eletrônico')
print('-=-' * 10)
saque = int(input('Qual valor você deseja sacar? '))
valor = saque
nota = 50
contagem = 0
print(f'Contando cédulas para o seu saque de R$ {saque:.2f}')
while True:
    if valor >= nota:
        valor -= nota
        contagem += 1
    else:
        if contagem > 0:
            print(f'{contagem} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        contagem = 0  # zerar a quantidade a cada mudança de nota
        if valor == 0:
            break
print('Volte sempre! Tenha um bom dia!')

# Esse programa poderia ser resolvido facilmente sem estrutura de repetição, mas não era a proposta do exercício:

'''
print('-=-' * 10)
print('Caixa eletrônico')
print('-=-' * 10)
saque = int(input('Qual valor você deseja sacar? '))
cinquenta = saque // 50
troco50 = saque - (cinquenta * 50)
vinte = troco50 // 20
troco20 = troco50 - (vinte * 20)
dez = troco20 // 10
troco10 = troco20 - (dez * 10)
um = troco10 // 1
print('-=-' * 10)
print('Quantidade de cédula sacadas:')
if cinquenta != 0:
    print(f'{cinquenta} notas de R$50.')
if vinte != 0:
    print(f'{vinte} notas de R$20.')
if dez != 0:
    print(f'{dez} notas de R$10.')
if um != 0:
    print(f'{um} notas de R$1.')
print('-=-' * 10)
'''
