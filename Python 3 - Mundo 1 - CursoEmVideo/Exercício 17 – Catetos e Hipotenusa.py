# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# import math # Importando a biblioteca 
from math import hypot #Importando somente o método hypot da biblioteca 

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
# Formula matemática de resolver a equação 

# hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
# print(f'Sendo o Cateto Oposto {co} e o Cateto Adjacente {ca}, a Hipotenusa será de {hipotenusa:.2f}')

#Importando a biblioteca do python
# hipotenusa = math.hypot(co, ca) # Usada quando importo a biblioteca inteira
hipotenusa = hypot(co, ca)
print(f'Sendo o Cateto Oposto {co} e o Cateto Adjacente {ca}, a Hipotenusa será de {hipotenusa:.2f}')



