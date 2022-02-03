# Exercício 011:

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2 m2.

l = float(input('Digite a largura da parede em metros:'))
a = float(input('Digite a altura da parede em metros:'))
print(f'Sua parede tem a dimensão de {l} x {a}, a área da parede é {l * a} m2 '
      f'e quantidade de tinta necessária para pintar a parede é {(l * a)/2:.2f} litros.')
