# Exercício 079:

'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o
número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.'''

valores = []
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
ordenada = sorted(valores)
print(f'Os valores únicos digitados em ordem crescente foram: {ordenada}')
