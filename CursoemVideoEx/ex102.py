# Exercício 102:

'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.'''


def fatorial(number=0, show=False):
    """
    => Função que calcula o fatorial de um número.
    :param number: número a ser calculado.
    :param show: mostra ou não os cálculos do fatorial.
    :return: fatorial do número.
    """
    number = int(input('Digite um número para saber seu fatorial: '))
    mostrar = str(input('Deseja ver os cálculos? [S/N] ')).strip().upper()[0]
    if mostrar in 'S':
        show = True
    factorial = 1  # o número 1 é o elemento nulo da multiplicação
    print(f'Calculando {number}! = ', end="")
    for counter in range(number, 0, -1):
        if show:
            print(f'{counter}', end="")
            print(' x ' if counter > 1 else ' = ', end='')  # restrição simplificada dentro de "print"
        factorial *= counter
        counter -= 1
    return f'{factorial}'


print(fatorial())
help(fatorial)
