# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Qual o seu nome completo: ').upper().strip()

print(f'Seu nome tem Silva? {"Silva" in nome}')