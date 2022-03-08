# Aula 019:

'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.'''


# Os dicionários são declarados em chaves e referenciados em colchetes.
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
# print(pessoa[0]) # Vai dar erro!
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# Lembrar de colocar aspas duplas na declaração de função feita com aspas simples.


# É importante entender todas as três estruturas dos dicionários:
# 1) As CHAVES são os índices;
# 2) Os VALORES são os conteúdos; e
# 3) Os ITENS são as duas coisas juntas.

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


# Essas estruturas também são acessíveis por laços:
for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')


# Dicionários são mutáveis:

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 78.6
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['peso']
for k, v in pessoas.items():
    print(f'{k} = {v}')

# Obs: Para incluir basta declarar a chave e o valor.
# Obs: Para excluir basta dar o comando "del" na chave.


# Dicionários funcionam dentro de outras estruturas como as listas, por exemplo:

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

# Obs: Se usarmos o comando "extend" ao invés do "append", o dicionário será desfeito e os itens entrarão com
# objetos na lista.

# Podemos dar entrada dos dados pelo teclado de maneira semelhante:

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla da UF: '))
    brasil.append(estado.copy())

# Opções de "print":

# Simples:
# print(brasil)

# Com laço para mostrar os dicionários por linha:
# for e in brasil:
#     print(e)

# Com laço duplo percorrendo lista e dicionário:
# for e in brasil:
#     for k, v in e.items():
#         print(f'O campo {k} tem valor {v}.')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

# Obs: Da mesma forma que nas listas temos que declarar que estamos apenas copiando os itens sem gerar uma relação
# entre eles com o comando "[:]", nos dicionários temos uma função interna ".copy()" para fazermos a cópia
# sem vincular os dados.

# Fim!
