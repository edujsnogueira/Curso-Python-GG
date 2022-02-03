# Aula 007:

# Operadores aritméticos:

# os operadores básicos são:
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão inteira

# exemplos de aplicação:
# 5 + 2 == 7
# 5 - 2 == 3
# 5 * 2 == 10
# 5 / 2 == 2.5
# 5 ** 2 == 25
# 5 // 2 == 2 (parte inteira da divisão)
# 5 % 2 == 1 (resto da divisão)

# Ordem de precedência dos operadores:

# primeiro lugar: () (parênteses)

# Obs: no Python só usa parênteses para operadores aritméticos, mas podemos usar vários parênteses juntos.
# (colchetes são usado para coleções (listas, tupla e dicionários) e chaves para

# segundo lugar: ** (potências)

# terceiro lugar: *, /, //, % (multiplicação, divisão, divisão inteira e resto da divisão)

# Obs: Não tem prioridade entres eles. O programa executa na ordem apresentada.

# quarto lugar: + - (soma e subtração)

# Prática:

# imprimindo o nome normalmente:
# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome}!')

# Fazendo aparecer em 20 caracteres:
# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:20}!')

# Fazendo aparecer centralizado em 20 caracteres:
# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:^20}!')

# Dicas de formatação: '=<' alinhado na esquerda, '=^'alinhado no centro e '=>'alinhado na direita.
# O que você colocar antes do sinal de alinhamento o programa preenche:

# Fazendo aparecer centralizado em 20 caracteres e com preenchimento:
# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer, {nome:=^20}!')

# Usando os operadores aprendidos na aula:

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2

print(f'A soma de {n1} e {n2} é {s}')
print(f'A subtração de {n1} e {n2} é {sub}')
print(f'A multiplicação de {n1} e {n2} é {m}')
print(f'A divisão de {n1} por {n2} é {d}')
print(f'A divisão inteira de {n1} por {n2} é {di}')
print(f'O resto da divisão de {n1} por {n2} é {r}')

# Obs: na divisão é possível escolher o número de casas decimais usando ':.nf',
# onde 'n' é o número de casas e 'f' indica que é float.

print(f'A divisão de {n1} por {n2} é {d:.3f}')

# Obs: É possível mandar apresentar o resultados na linha de baixo com '\n'
# ou mandar apresentar na mesma linha com 'end='''.

print(f'A soma é {s} \n A subtração é {sub} \n A multiplicação é {m}', end=' ')
print(f'A divisão é {d}')
