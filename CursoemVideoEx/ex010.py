# Exercício 010:

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar:

d = float(input('Quanto dineiro você tem na carteira? R$'))
print(f'Com R$ {d} você pode comprar US$ {d / 5.31:.2f} ou € {d / 6.06:.2f}.')
