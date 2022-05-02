# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite sua velocidade  '))
velocidadeMaxima = 80
multa = 7

# pagar = velocidade - velocidadeMaxima * 

if velocidade > velocidadeMaxima:
    print(f'Você foi multado\nDeverá pagar uma multa de R$ {(velocidade - velocidadeMaxima)*multa},00')
else: 
    print('Dirija com segurança!')
