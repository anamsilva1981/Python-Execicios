# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Importa a biblioteca
import random

#Recebe as informações
alunoUm = input(' Primeiro aluno: ')
alunoDois = input(' Segundo aluno: ')
alunoTres = input(' Terceiro aluno: ')
alunoQuarto = input('Quarto aluno: ')

#Cria uma lista com todos os nomes dentro dela
lista = [alunoUm, alunoDois, alunoTres, alunoQuarto]

#Embaralha os nomes dentro da lista 
random.shuffle(lista)

print(f'A ordem de apresentação será {lista}')

