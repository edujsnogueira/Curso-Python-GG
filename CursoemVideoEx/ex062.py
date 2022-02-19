# Exercício 062:

'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que queremos mostrar 0 termos.'''

# Tinha um entendimento diferente do problema. Acreditei que o objetivo era escolher a quantidade de termos:

'''
termos = 1
while termos != 0:
    primeiro = int(input('Digite o primeiro termo de uma progressão aritmética: '))
    razao = int(input('Digite a razão da progressão aritmética: '))
    termos = int(input('Digite quantos termos você quer calcular. Se você digitar 0 o programa vai encerrar: '))
    soma = primeiro
    contador = 1
    if termos != 0:
        while contador <= termos:
            print(f'O {contador}° termo é {soma}.')
            contador += 1
            soma += razao
    else:
        print('Encerrando.....')
print('Fim!')
'''


# Mas é possível fazer da forma como o professor comentou no vídeo:


primeiro = int(input('Digite o primeiro termo de uma progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
soma = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'O {contador}° termo é {soma}.')
        contador += 1
        soma += razao
    print('Pausa...')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print(f'Progressão finalizada com {total} termos mostrados!')
