# Exercício 061:

'''Refaça o exercício 051, lendo o primeiro termo e a razão de uma progressão aritmética, mostrando os dez primeiros
termos da progressão, usando a estrutura "while".'''


primeiro = int(input('Digite o primeiro termo de uma progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
soma = primeiro
contador = 1
while contador <= 10:
    print(f'O {contador}° termo é {soma}.')
    contador += 1
    soma += razao
print('Fim!')
