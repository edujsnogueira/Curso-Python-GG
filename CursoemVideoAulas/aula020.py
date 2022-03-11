# Aula 020:

'''Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando "def" em Python e como utilizá-lo com parâmetros simples e múltiplos.'''

# As funções servem para substituir os comandos repetitivos.

# Como exemplo, vamos substituir os comando de imprimir linhas:

def lin():
    print('-=' * 30)


lin()
print('CURSO EM VÍDEO'.center(60))
lin()
lin()
print('APRENDA PYTHON'.center(60))
lin()
lin()
print('GUSTAVO GUANABARA'.center(60))
lin()


# O comando também serve para estabelecer parâmetros:

def mensagem(txt):
    print('-=' * 30)
    print(txt.center(60))
    print('-=' * 30)


mensagem('CURSO EM VÍDEO')
mensagem('APRENDA PYTHON')
mensagem('GUSTAVO GUANABARA')


# As declarações de parâmetros podem ser explícitas ou implícitas:

def soma(a, b):
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma de A e B é {s}.')


# Programa principal:
soma(4, 5)
soma(a=4, b=5)
soma(b=4, a=5)
# A declaração pode ser fora da ordem estabelecida na definição da função.

# soma(a=4, 5) # Esse comando vai dar erro, pois só é possível deixar as variáveis declaradas ou não. Não é possível
# misturar os dois casos.

# soma(3, 4, 9) # Esse comando também vai apresentar erro, pois só existem duas variáveis na função soma.


# Entretanto, é possível definir um número não declarado de variáveis com a função de empacotamento com o "*":
# O empacotamento cria uma "tupla" que pode ser operada com os mesmos parâmetros vistos anteriormente:

def contador(* valor):
    print(valor)
    print(len(valor))


contador(2, 3)
contador(2, 5, 6, 8, 9, 0)
contador(2, 5, 9)


# Também é possível definir funções sobre uma lista, que entre outras vantagens, pode ser mudada:

def dobra(lista):
    for k in range(0, len(lista)):
        lista[k] *= 2


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# Fim!
