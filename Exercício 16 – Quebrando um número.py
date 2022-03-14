# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc # Importando somente a função trunc da biblioteca math

num = float(input('Digite um numero: '))

print(f' Você digitou o numero {num} e sua portção inteira é {trunc(num)}') 
# Exibindo a porção inteira com a função trunc da biblioteca Math

print(f'O valor digitado foi {num} e sua porção inteira é {int(num)}')
#Exibindo a porção inteira com "int"