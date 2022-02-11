# Exercício 029:

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar a velocidade de 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km/h acima do limite!

velocidade = int(input('Digite a velocidade do carro em km/h!'))
if velocidade > 80:
    print(f"Você foi multado! A sua velocidade era de {velocidade}km/h e o limite era de 80km/h.")
    print(f"O valor da sua multa é R$ {(velocidade - 80) * 7}")
else:
    print("Parabéns! Você é um motorista cuidadoso!")
