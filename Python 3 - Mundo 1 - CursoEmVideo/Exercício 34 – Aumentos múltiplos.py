# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salarioAtual = int(input('Informe o salário atual '))

if salarioAtual <= 1250:
    print(f'O valor do salário com ajuste é de R$ {salarioAtual * 1.15:.2f}')
else:
    print(f'O valor do salário ajustado é de R$ {salarioAtual * 1.10:.2f}')