# Exercício 048:

'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que
se encontram no intervalo de 1 até 500.'''

soma = 0 # acumulador
contador = 0 # contador
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        print(contagem) # não foi pedido no exercício, apenas para teste.
        soma = soma + contagem
        contador = contador + 1 # pode usar '+=' no Python
print(f'Foram contados {contador} números e a soma dos números ímpares múltiplos de três é {soma}.')
