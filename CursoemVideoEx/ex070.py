# Exercício 070:

'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. Ao final, mostre:
a) qual o total gasto na compra;
b) quantos produtos custam mais de R$ 1.000,00;
c) qual é o nome do produto mais barato.'''

print('-=-' * 10)
print('Lista de compras:')
print('-=-' * 10)
produtos = caros = total = menor = 0
barato = " "
while True:
    nome = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço do produto: R$ '))
    total += preco
    produtos += 1
    if menor == 0: # o bloco posterior poderia ser colocado aqui com a cláusula "or".
        barato = nome
        menor = preco
    else:
        if preco < menor:
            barato = nome
            menor = preco
    if preco > 1000:
        caros += 1
    compra = str(input('Quer continuar comprando? [S/N] ')).strip().upper()[0]
    if compra in 'S':
        print('-=-' * 10)
        print('Lista de compras:')
        print('-=-' * 10)
    if compra in 'N':
        break
print(f'Você comprou {produtos} produtos e o total da compra foi de R$ {total:.2f}\n'
      f'Você comprou {caros} produtos que custaram mais de R$ 1.000,00\n'
      f'O nome do produto mais barato é {barato} e ele custou R$ {menor:.2f}')
