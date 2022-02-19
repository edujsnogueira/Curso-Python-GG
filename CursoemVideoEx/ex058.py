# Exercício 058:

'''Melhore o jogo do exercício 028, onde o computador vai "pensar" um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''


import random

print('O computador está escolhendo um número inteiro entre 0 e 10...')
computador = random.randint(0, 10)
palpites = 1
jogador = int(input('O computador já escolheu um número inteiro entre 0 e 10. Qual o seu palpite?'))
while computador != jogador:
    palpites += 1
    if computador > jogador:
        jogador = int(input('O computador pensou em um número maior. Tente outra vez:'))
    else:
        jogador = int(input('O computador pensou em um número menor. Tente outra vez:'))
print(f'Parabéns, você venceu! Você precisou de {palpites} tentativas para adivinhar o número correto.')
