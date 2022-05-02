#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioAtual = float(input('Digite o salário Atual: '))

print(f'''
    Salario Atual R${salarioAtual:.2f}
    Salário com Reajuste R$ {salarioAtual *1.15:.2f}
''')