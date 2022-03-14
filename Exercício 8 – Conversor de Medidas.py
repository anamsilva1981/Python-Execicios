# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Informe a medida em Metros: '))

print(f'''
    {metros} é referente a:
    {metros*100} Centímetros,
    {metros*1000} Milímetros.
''')