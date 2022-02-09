# Exercício 022:

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas.
# 2) O nome com todas as letras minúsculas.
# 3) Quantas letras ao todo (sem considerar os espaços)
# 4) Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo:')).strip()
# Obs: o 'strip'já elimina os espaços desnecessários antes e depois

print(f'O seu nome com todas as letras maiúsculas é: {nome.upper()}')
print(f'O seu nome com todas as letras minúscula é: {nome.lower()}')
print(f'O seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print(f'O seu primeiro nome tem {nome.find(" ")} letras.')
# Obs: o 'find' já retornou o primeiro espaço vazio, que já é a resposta.

# Alternativa criando uma lista:
dividido = nome.split()
print(f'O seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras.')
