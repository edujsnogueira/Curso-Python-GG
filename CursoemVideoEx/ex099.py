# Exercício 099:

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* valor):
    if not valor:
        print('-=' * 30)
        print('Analisando os valores passados...')
        print('Não foi passado nenhum valor!')
    else:
        print('-=' * 30)
        print('Analisando os valores passados...')
        print(f'Foram passados {len(valor)} valores ao todo: {valor}')
        print(f'O maior valor informado foi {max(valor)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
