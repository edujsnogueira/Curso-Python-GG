# Aula 017:

'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas
que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.'''


# num = (2, 5, 9, 1)
# print(num)
# num[2] = 3 # Vai dar erro! Tuplas são imutáveis!


# Listas são mutáveis!
num2 = [2, 5, 9, 1]
print(num2)
num2[2] = 3
print(num2)


# Mas não podemos adicionar elementos com simples atribuição!
# nun2[4] = 7 # Vai dar erro!


# para adicionar usamos o comando 'append'.
num2.append(7)
print(num2)


# Podemos ordenar com o "sort":
num2.sort()
print(num2)
num2.sort(reverse=True)
print(num2)


# Função "len" retorna a quantidade de elementos:
print(f'A lista num2 tem {len(num2)} elementos!')


# Podemos inserir elementos em qualquer posição da lista:
num2.insert(2, 0) # Posição e elemento adicionado
print(num2)


# O comando "pop" sem parâmetro elimina o último elemento:
num2.pop()
print(num2)


# Mas também podemos definir o elemento que queremos eliminar:
num2.pop(2)
print(num2)


# Podemos eliminar com o comando remove indicando um elemento, ao invés de indicarmos um índice.
# Se o elemento estiver repetido, somente o primeiro será eliminado (podemos eliminar todos usando
# laços de repetição).
num2.append(7)
print(num2)
num2.remove(7)
print(num2)

# Se mandar eliminar um elemento inexistente vai dar erro (a menos que usemos o "if").
# num2.remove(4)


# Podemos mostrar os valores (e os índices) com estruturas de repetição:
valores = num2
for valor in valores:
    print(f'{valor}')

for chave, valor in enumerate(valores):
    print(f'O valor {valor} está na posição {chave}.')

# Podemos ler os valores de uma lista por meio do teclado também!

# numeros = list()
# for cont in range(0, 5):
#     numeros.append(int(input('Digite um valor: ')))
# print(numeros)


# Uma opção mais direta:
# numeros = list(int(input('Digite um valor: ')) for cont in range(0, 5))
# print(numeros)


# Se você mandar uma lista receber os elementos de outra elas se vinculam, e uma alteração em uma altera a outa também!

a = [2, 3, 4, 7]
b = a
print(f'A lista A é {a}')
print(f'A lista B é {b}')
b[2] = 8
print(f'A lista A é {a}')
print(f'A lista B é {b}')

# Mas é possível mandar uma lista apenas receber todos os elementos de outra sem criar o vículo:

a = [2, 3, 4, 7]
b = a[:] # A lista "b" recebe todos os elementos da lista "a" sem criar um vínculo entre elas.
print(f'A lista A é {a}')
print(f'A lista B é {b}')
b[2] = 8
print(f'A lista A é {a}')
print(f'A lista B é {b}')

# Fim!
