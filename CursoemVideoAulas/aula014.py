# Aula 014:

'''Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.'''

# Laços de Repetição (continuação).

# Estrutura de repetição com teste lógico (while):

'''
# Estrutura de contagem com "for", visto anteriormente:
for c in range(1, 10):
    print(c)
print('Fim!')
'''

# Estrutura de contagem com "while"
'''
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim!')
'''

# Quando você não sabe quantas iterações serão necessárias (range) você tem que usar o "while".
'''
n = 1
while n != 0: # essa é a condição de parada
    n = int(input('Digite um número inteiro:'))
print('Fim!')

# Obs: O programa vai continuar rodando até o usuário digitar "0".
'''


# Contagem de números pares e ímpares sem limite definido:

n = 1
par = 0
impar = 0
while n != 0: # essa é a condição de parada
    n = int(input('Digite um número inteiro:'))
    if n != 0: # para não contar o zero de escape como número par.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')

# Fim!
