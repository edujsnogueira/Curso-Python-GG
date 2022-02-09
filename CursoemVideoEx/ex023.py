# Exercício 023:

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
'''Exemplo: Digite um número: 1843
unidade: 4
dezenas: 3
centenas: 8
milhar: 1'''

# Obs: É possível resolver o problema por string e por operadores matemáticos.

# Operadores matemáticos:
'''numero = int(input('Digite um número entre 0 e 9999:'))
print(f'Analisando o número {numero}...')
print(f'unidade:{numero // 1 % 10}')
print(f'dezena:{numero // 10 % 10}')
print(f'centena:{numero // 100 % 10}')
print(f'milhar:{numero // 1000 % 10}')'''
# A lógica é pegar a parte inteira da divisão com o comando "//" e depois pegar a parte decimal com o "%".


# String
numero = str(input('Digite um número entre 0 e 9999:')).strip().zfill(4)
print(f'Analisando o número {numero}...')
print(f'unidade:{numero[3]}')
print(f'dezena:{numero[2]}')
print(f'centena:{numero[1]}')
print(f'milhar:{numero[0]}')
# Obs: Sempre que usar string é bom usar o "strip" para tirar os espaços antes e depois!
# Obs: O comando "zfill" resolve o problema de digitação de números com memos de 4 dígitos!
