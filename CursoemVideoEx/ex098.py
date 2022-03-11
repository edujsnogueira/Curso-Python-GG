# Exercício 098:

'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1;
b) de 10 até 0, de 2 em 2; e
c) uma contagem personalizada.'''

from time import sleep


def contador(c, f, p):
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1:')
    for k in range(1, 11):
        print(f'{k}', end=' ')
        sleep(0.1)
    print('FIM!')
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2:')
    for k in range(10, -1, -2):
        print(f'{k}', end=' ')
        sleep(0.1)
    print('FIM!')
    print('-=' * 20)
    print('Agora é a sua vez de personalizar a contagem!')
    c = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p == 0:
        p = 1
    if c > f:
        if p > 0:
            p *= -1
    if f > c:
        if p < 0:
            p *= -1
    if f == c:
        print(f'{f}')
    else:
        print(f'Contagem de {c} até {f} de {p} em {p}:')
        for k in range(c, f, p):
            print(f'{k}', end=' ')
            sleep(0.1)
    print('FIM!')
    print('-=' * 20)


contador(1, 1, 1)
