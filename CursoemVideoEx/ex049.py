# Exercício 049:

'''Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, so que agora utilizando o
laço for.'''

n = int(input('Digite um número inteiro para ver a tabuada:'))
print(f'A tabuada de {n} é:')
for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')
