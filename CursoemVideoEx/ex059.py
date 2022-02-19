# Exercício 059:

'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar;
[2] multiplicar;
[3] maior;
[4] novos números; ou
[5] sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso.'''


n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor:'))
menu = 0
while menu != 5:
    menu = int(input('''Opções disponíveis:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Qual opção você deseja escolher?'''))
    if menu == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    elif menu == 2:
        print(f'A multiplicação de {n1} por {n2} é {n1 * n2}.')
    elif menu == 3:
        print(f'Você digitou {n1} e {n2} e o maior deles é {max(n1, n2)}.')
    elif menu == 4:
        print('Escolha novos números:')
        n1 = float(input('Digite o primeiro valor:'))
        n2 = float(input('Digite o segundo valor:'))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
    print('-=-' * 20)
print('Fim!')
