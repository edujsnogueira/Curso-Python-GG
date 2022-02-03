# Exercício 012:

# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Digite o preço do produto em Reais:'))
print(f'O produto que custava {p}, com desconto de 5%, deve ser vendido por R$ {p * 0.95:.2f}.')
