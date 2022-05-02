# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um numero com 4 casas decimais: '))

print(f'Analisando o numero {numero}')

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'''
O numero digitado tem: 
{u} Unidades
{d} Dezenas
{c} Centenas
{m} Milhares
''')



