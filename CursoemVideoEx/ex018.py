# Exercício 018:

# Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo:

import math
angulo = float(input('Digite um ângulo em graus:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo digitado foi {angulo} graus, o seno mede {seno:.2f}, '
      f'o cosseno mede {cosseno:.2f}, e a tangente mede {tangente:.2f}.')

# Obs: as fórmulas trigonométricas em 'math' só funcionam em radianos, por isso foi necessário converter para graus.
