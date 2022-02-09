# Exercício 025

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no mome.

nome = str(input('Digite seu nome completo:')).lower().strip()
print(f'Você possui Silva no seu nome? {"silva" in nome}')
# Obs: do mesmo modo que o anterior, sempre é bom tirar os espaços desnecessários e transformar tudo para maiúsculo
# ou minúsculo para facilitar a comparação.
