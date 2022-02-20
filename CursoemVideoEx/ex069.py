# Exercício 069:
'''Crie um programa que leia a idade e o sexo de vária pessoas. A cada pessoa cadastrada o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres têm menos de 20 anos.'''

print('-=-' * 10)
print('Cadastro de pessoas:')
print('-=-' * 10)
maiores = homens = mulheres = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: [M/F]')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F': # a idade poderia ser juntada aqui com a cláusula "and".
        if idade < 20:
            mulheres += 1
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'S':
        print('-=-' * 10)
        print('Cadastro de pessoas:')
        print('-=-' * 10)
    else:
        break
print(f'O total de pessoas com mais de 18 anos é {maiores}.\n'
      f'Ao todo temos {homens} homens cadastrados.\n'
      f'Temos {mulheres} mulheres com menos de 20 anos.')
