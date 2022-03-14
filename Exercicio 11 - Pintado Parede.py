#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
import math

altura = float(input('Digite a altura da parede '))
largura = float(input('Digite a largura da parede '))

# lata = 2

# ;tinta = (largura * altura) / 2

print(f'''
    Area total da parede: {altura * largura:.2f}
    Quantidade de latas necessárias: {math.ceil((altura * largura)/2):.0f}
''')