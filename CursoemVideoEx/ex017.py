# Exercício 017:

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.

# import math
# oposto = float(input('Digite o comprimento do cateto oposto do triângulo retângulo:'))
# adjacente = float(input('Digite o comprimento do cateto adjacente do triângulo retânculo:'))
# print(f'O cateto oposto mede {oposto}, o cateto adjacente mede {adjacente} e a \n'
#       f'hipotenusa mede {math.sqrt(oposto ** 2 + adjacente ** 2)}.')

# Podemos executar direto o cálculo da hipotenusa com a função específica:

'''import math
oposto = float(input('Digite o comprimento do cateto oposto do triângulo retângulo:'))
adjacente = float(input('Digite o comprimento do cateto adjacente do triângulo retânculo:'))
print(f'O cateto oposto mede {oposto}, o cateto adjacente mede {adjacente} e a \n'
      f'hipotenusa mede {math.hypot(oposto, adjacente)}.')'''

# O exercício também pode ser feito sem importar nenhuma bilioteca:

oposto = float(input('Digite o comprimento do cateto oposto do triângulo retângulo:'))
adjacente = float(input('Digite o comprimento do cateto adjacente do triângulo retânculo:'))
print(f'O cateto oposto mede {oposto}, o cateto adjacente mede {adjacente} e a \n'
      f'hipotenusa mede {(oposto ** 2 + adjacente ** 2) ** (1/2):.2f}.')
