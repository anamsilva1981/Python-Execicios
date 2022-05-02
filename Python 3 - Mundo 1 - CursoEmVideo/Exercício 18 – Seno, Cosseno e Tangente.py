# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math #Importando biblioteca de matemática
angulo = float(input('Digite o angulo que deseja obter: '))

#Calculando o ANGULO
seno = math.sin(math.radians(angulo))  #Calculando o seno do angulo
print(f'O ÂNGULO de {angulo} tem o SENO de {seno:.2f}')

coseno = math.cos(math.radians(angulo)) #Calculando o Coseno de um angulo
print(f'O angulo de {angulo} tem o COSENO de {coseno:.2f}')

tangente =math.tan(math.radians(angulo)) #Calculando a TANGENTE de um angulo
print(f'O ANGULO de {angulo} tem a TANGENTE de {tangente:.2f}')