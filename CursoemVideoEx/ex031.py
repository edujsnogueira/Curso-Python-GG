# Exercício 031:

# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50
# por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = int(input('Digite a distância da sua viagem em km:'))
if distancia <= 200:
    print(f"Sua viagem possui uma distância de {distancia}km e o valor da passagem é de R$ {distancia * 0.5}")
else:
    print(f"Sua viagem possui uma distância de {distancia}km e o valor da passagem é R$ {distancia * 0.45}.")
