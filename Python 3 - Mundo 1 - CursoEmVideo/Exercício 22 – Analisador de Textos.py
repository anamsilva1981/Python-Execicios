# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:


nome = str(input('Digite seu nome completo: '))

# – O nome com todas as letras maiúsculas e minúsculas.
print(f'Seu nome em caixa alta {nome.upper()}')
print(f'Seu nome em caixa baixa {nome.lower()}')

# – Quantas letras ao todo (sem considerar espaços).
print(f' Seu nome tem {len(nome)-nome.count(" ")} caracteres')

# – Quantas letras tem o primeiro nome.
print(f'Seu 1º nome tem {nome.find(" ")} letras')
