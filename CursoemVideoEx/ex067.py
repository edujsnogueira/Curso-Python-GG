# Exercício 067:

'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''


while True:
    print('-' * 50)
    numero = int(input('Digite um número inteiro para saber a tabuada. \n'
                       'Se o número for negativo o programa será encerrado: '))
    if numero < 0:
        break
    print('-' * 50)
    for c in range(1, 11):
        print(f'{c} X {numero} = {c * numero}')
print('Fim!')
