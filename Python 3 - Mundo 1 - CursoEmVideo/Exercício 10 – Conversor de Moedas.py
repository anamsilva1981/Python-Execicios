# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Digite o valor em reais: '))

print(f'Você tem ${(carteira / 5.01):.2f}')