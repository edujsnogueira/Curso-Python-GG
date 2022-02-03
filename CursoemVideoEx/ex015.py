# Exercício 015:

# Escreva um programa que pergunte a quantide de quilômetros percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por
# km rodado.

d = int(input('Digite a quantidade de dias alugados'))
km = float(input('Digite a quantidade de Km rodados:'))
print(f'O preço a pagar por alugar o carro por {km} km e {d} dias é de R$ {km * 0.15 + d * 60:.2f}.')
