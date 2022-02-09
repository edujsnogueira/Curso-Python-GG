# Exercício 026

# Faça um programa que leia uma frase pelo teclado e mostre:
# 1) Qunatas vezes aparece a letra "a".
# 2) Em que posição ela aparece a primeira vez.
# 3) Em que posição ela aprece a última vez.

frase = str(input('Digite uma frase:')).strip().upper()
print(f'A letra a aparece {frase.count("A")} vezes na frase acima!')
print(f'A primeira ocorrência da letra a é na posição {frase.find("A") + 1}.')
print(f'A última ocorrência da letra a é na posição {frase.rfind("A") + 1}.')

'''Obs: O programa ainda daria um erro por causa das variações de a com acentuação. Se quisermos ignorar a acentuação
e contarmos todas as variantes como letra a, exite o pacote "unidecode" que faz a transformação.'''
