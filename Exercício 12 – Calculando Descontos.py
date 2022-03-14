#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto '))

acrescimo = 1.05

print(f'''
    Preço antigo {preco}
    Preço com reajuste {preco * acrescimo}
''')