# Aula 016:

'''Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis
compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por
chaves individuais.'''

# Variáveis compostas (Tuplas):

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche)

# Obs: Os parênteses para marcar a tupla são opcionais no Python. O comando funciona simplesmente com a enumeração:

lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim'
print(lanche)

# A estrutura de Tupla aceita o fatiamento do mesmo modo que a string:
print(lanche[1]) # segundo termo
print(lanche[-1]) # primeiro termo de trás pra frente
print(lanche[0]) # primeiro termo
print(lanche[-0]) # primeiro termo
print(lanche[1:3]) # do segundo termo (inclusive) até o quarto termo (exclusive)
print(lanche[2:]) # do terceiro termo em diante
print(lanche[:2]) # do primeiro termo até o terceiro (exclusive)
print(lanche[::]) # tudo

# Tuplas são IMUTÁVEIS
print(lanche[1])
# lanche[1] = 'refrigerante' # comando vai gerar erro

# Também podemos usar estruturas de repetição com a tupla:

# lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}!')
print('Comi para caramba!')

# Também podemos combinar o "range" com o "len" para as estruturas de repetição:

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]}!')
print('Comi para caramba!')

# O resultado dos dois exemplos acima é o mesmo.

# Também podemos descobrir a posição relativa de cada elemento com o "enumerate" ou com o "renge".

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for contador, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na  posição {contador}!')
print('Comi para caramba!')

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}!')
print('Comi para caramba!')

# Podemos ordenar a apresentação dos itens da tupla (Embora a ordem seja imutável, o "print" vai ser ordenado).
# Interessante notar que o Python cria uma lista para fazer essa ordenação.

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
print(sorted(lanche[0])) # criou uma lista ordenada com as letras do primeiro elemento na ordem normal!!!
print(lanche)


# Também podemos fazer operações com tuplas:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a # A ordem é importante. Os elementos não são somados, são concatenados.
print(a)
print(b)
print(c)
print(d)

# Existem algumas funções internas:

print(c.count(5))
# Conta quantas vezes o elemento aparece repetido na tupla.

# Podemos saber a posição do elemento na tupla:
print(c.index(8))

# Se o elemento aparecer mais de uma vez o "index" retorna a primeira ocorrência:
print(d.index(2))

# Você pode usar o deslocamento para saber quala próxima posição do elemento repetido:
print(d.index(5, 1))

# No exemplo acima, como eu sei que existe um número cinco na posição "0", eu desloco o início da busca para a
# posição "1" e descubro onde existe outro elemento "5".

# Tuplas aceitam elementos de diversos tipos:

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

# Por fim, podemos deletar uma tupla inteira:
del(pessoa)
print(pessoa)

# Fim!
