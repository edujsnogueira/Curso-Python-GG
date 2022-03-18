# Aula 021:

'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive
Help em Python, o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais
dinamismo em funções Python, escopo de variáveis e retorno de resultados.'''

# Existem algumas maneiras para obter ajuda no Python. Uma das possibilidades é o "interactive help""

# A primeira e colocar o comando "help" com a função que você deseja entre os parênteses:

help(print)


# Também é possível obter a documentação da função com o uso do "print":

print(print.__doc__)


# Quando criamos funções podemos escrever "docstrings".
# As "docstrings" são escritas logo após a "def". É só digitar 3 aspas duplas para abrir a "docstring".


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem;
    :param f: fim da contagem;
    :param p: passo da contagem;
    :return: sem retorno.
    -> Função criada por Gustavo Guanabara do Curso em Vídeo.
    """
    c = i
    while c <= f:
        print(f'{c}', end="")
        c += p
        print('Fim!')


help(contador)


# Parâmetros opcionais são os valores padrão caso algum (ou todos) os parâmetros não sejam informados.
# Todos os parâmetros podem receber o valor padrão, basta colocar a atribuição do valor padrão na declaração da função.


def soma(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')


soma(3, 2, 5)
soma(8, 4)


# Escopo de variáveis.
# Quando uma variável é definida no programa principal el pode ser chamada no programa secundário normalmente,
# pois ela é uma variável global.
# Ao contrário, se a variável só for definida no programa secundário ela é apenas uma variável local:


def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


# Programa principal:
n = 2
teste()
print(f'No programa principal, n vale {n}.')
# print(f'No programa principal, x vale {x}.') # Vai dar erro pois a variável x é local.

# Prestar atenção, pois a mesma variável pode ser definida tanto com escopo global quanto com escopo local:


def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A variável "A" local vale {a}.')
    print(f'A variável "B" local vale {b}.')
    print(f'A variável "C" local vale {c}.')


a = 5
teste(a)
print(f'A variável "A" global vale {a}.')
# print(f'A variável "B" global vale {b}.') # Não foi definida.
# print(f'A variável "C" global vale {c}.') # Não foi definida.


# Para que a alteração feita pelo comando local ocorra também no escopo global é só colocar a função "global":


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A variável "A" local vale {a}.')
    print(f'A variável "B" local vale {b}.')
    print(f'A variável "C" local vale {c}.')


a = 5
teste(a)
print(f'A variável "A" global vale {a}.')
# print(f'A variável "B" global vale {b}.') # Não foi definida.
# print(f'A variável "C" global vale {c}.') # Não foi definida.


# Retorno de valores:

# O retorno de valores pode ser efetuado com a função "return":


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)


print(f'As somas valem {r1}, {r2} e {r3} respectivamente.')

# Fim!
