# Exercício 080:

'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

valores = []
for num in range(0, 5):
    valor = int(input(f'Digite um valor: '))
    if num == 0 or valor > valores[-1]:
        print(f'O valor {valor} foi adicionado ao final da lista!')
        valores.append(valor)
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                print(f'O valor {valor} será adicionado na posição {pos}.')
                valores.insert(pos, valor)
                break
            pos += 1
print(f'O valores digitados em ordem foram: {valores}.')
