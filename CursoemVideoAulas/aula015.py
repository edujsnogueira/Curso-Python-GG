# Aula 015:

'''Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas
estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos
interromper um laço no meio do caminho. Além disso, vamos aprender como trabalhar com as novas fstrings
do Python.'''

# Laços de Repetição:

# Repetição normal:

'''
cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('Fim!')
'''


# Repetição infinita (tem que interromper o programa para o computador não travar):

'''
cont = 1
while True:
    print(cont, ' ', end='')
    cont += 1
print('Fim!')
'''

# Repetição infinita com parada:

numero = soma = 0
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 999:
        break
    soma += numero
print(f'A soma dos números digitados é {soma}.')

