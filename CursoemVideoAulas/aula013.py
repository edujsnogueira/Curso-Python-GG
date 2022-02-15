# Aula 013:

'''Nessa aula, vamos começar os nossos estudos com os laços e vamos fazer primeiro o "for",
que é uma estrutura versátil e simples de entender.'''

# Laços de Repetição:

# Estrutura de Repetição com variável de controle (for):

'''
# Repetindo um comando simples: (lembrar qu eo Python ignora o último comando!)

for c in range(0, 6):
    print('Oi!')
print('Fim!')



# Criando uma contagem: (Quero imprimir de 1 até 6, por isso colocamos o 7 no final.)

for c in range(1, 7):
    print(c)
print('Fim!')



# Também pode ser feito para contagem regressiva (tem que colocar o comando para diminuir ao final.):

for c in range(6, 0, -1):
    print(c)
print('Fim!')



# Também pode ser feito com outros comandos (pulando a cada dois, por exemplo.)

for c in range(6, 0, -2):
    print(c)
print('Fim!')



# Também pode ser feito com uma variável atribuída.

n = int(input('Digite um número inteiro menor até 10:'))
for c in range(0, n + 1):
    print(c)
print('Fim!')



# Ou com todas as variáveis atribuídas:

inicio = int(input('Digite o início da contagem:'))
final = int(input('Digite o final da contagem:'))
passo = int(input('Digite o passo da contagem:'))
for c in range(inicio, final + 1, passo):
    print(c)
print('Fim!')
'''


# Podemos colocar as entradas no interior do laço, para fazer coisas práticas como obter a soma, por exemplo:

soma = 0
for c in range(0, 4):
    n = int(input('Digite um número:'))
    soma = soma + n
print(f'A soma dos números digitados foi {soma}.')

# Fim!
