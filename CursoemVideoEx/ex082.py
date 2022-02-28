# Exercício 082:

'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas.'''


valores = []
pares = []
impares = []
while True:
    valor = int(input('Digite um número inteiro para criarmos uma lista: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não foi adicionado!')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos! Digite apenas [S/N] par continuar ou parar! ')).upper().strip()[0]
    if continuar in 'N':
        break
for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
valores.sort()
pares.sort()
impares.sort()
print(f'A lista de valores digitados foi {valores}.')
print(f'A lista de valores pares digitados foi {pares}.')
print(f'A lista de valores ímpares digitados foi {impares}.')
