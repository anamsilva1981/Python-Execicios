# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Quantos KM foram percorridos no percurso? '))

if distancia < 200:
    print(f' O preço da passagem é de R${distancia*0.50:.2f}')
else:
    print(f'O valor da pagassem é de R${distancia*0.45:.2f}')


