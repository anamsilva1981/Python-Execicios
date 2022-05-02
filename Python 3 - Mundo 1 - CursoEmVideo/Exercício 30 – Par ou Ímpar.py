# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um numero qualquer '))
resultado = numero % 2

if resultado == 0:
    print('Você digitou um numero PAR')
else: 
    print('Você digitou um número IMPAR')
