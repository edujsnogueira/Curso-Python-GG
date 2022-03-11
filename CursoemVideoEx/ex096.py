# Exercício 096:

'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''


def d(l, c):
    print(f'A área de um terreno de dimensões de {l} x {c} é de {l * c}.')


print('Controle de terrenos'.center(60))
print('-=' * 30)
l = float(input('Digite a largura do terreno (m): '))
c = float(input('Digite o comprimento do terreno (m): '))
d(l, c)
