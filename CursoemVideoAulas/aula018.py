# Aula 018:

'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis
compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.'''

# Listas compostas:

teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# Observação: se não colocarmos os dois pontos ocorre uma vinculação total e não uma cópia,
# e a alteração mudaria todas as duas listas.

# Podemos usar os índices tanto na lista maior quanto nas listas internas:
pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[2][1])

# Podemos usar os índices nas estruturas de repetição:
for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

# Também podemos usar as estruturas de repetição para termos a entrada dos dados:

povo = []
dado = []
for c in range(0, 4):
    dado.append(str(input('Digite um nome: ')).strip().capitalize())
    dado.append(int(input('Digite a idade: ')))
    povo.append(dado[:])
    dado.clear()
print(povo)


# Podemos também verificar dados nas estruturas de repetição:

maiores = menores = 0
for p in povo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maiores += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menores += 1

print(f'Temos o total de {maiores} maiores e {menores} menores de idade.')

# Fim!
