# Exercício 081:

'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''


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
valores.sort(reverse=True)
print(f'Foram adicionados {len(valores)} números distintos.')
print(f'A lista dos números adicionados em ordem decrescente é {valores}.')
print(f'O valor 5 foi digitado e está na lista!' if 5 in valores else 'O valor 5 não está na lista!')
