# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmsPercorrido = float(input('Digite a quantidade de Kms percorridos: ')) 
aluguel = int(input('Informe a quantidade de dias alugado: '))

diaria = 60
kmRodado = 0.15

print(f'''
    Dias locados: {aluguel}
    Kms percorridos: {kmsPercorrido}
    Valor total das diárias: {aluguel *  diaria}
    Valor total da Kilometragem: {kmRodado * kmsPercorrido}
    Total a ser pago: {(aluguel *  diaria) + (kmRodado * kmsPercorrido) }
''')