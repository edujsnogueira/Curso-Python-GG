# Aula 022:

'''Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python
e reutilizar nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote,
ampliando ainda mais a modularização em grandes projetos em Python.'''


def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


# Programa principal:
num = int(input('Digite um valor para saber o seu fatorial: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
