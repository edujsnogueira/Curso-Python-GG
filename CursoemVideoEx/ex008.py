# Exercício 008:

# Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros:

m = float(input('Digite uma distância em metros:'))
print(f'A distância {m} metros equivale a: \n {m / 1000} kilômetros, \n {m / 100} hectômetros, \n '
      f'{m / 10} decâmetros, \n {m * 10:.2f} decímetros, \n {m * 100:.2f} centímetros \n {m * 1000:.2f} milímetros.')
