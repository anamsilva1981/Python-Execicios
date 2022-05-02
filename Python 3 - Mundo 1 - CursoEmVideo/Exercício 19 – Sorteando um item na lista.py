# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random # Importando randomizador de elementos
alunoUm = input('Primeiro aluno: ')
alunoDois = input('Segundo aluno: ')
alunoTres = input('Terceiro aluno: ')
alunoQuatro = input('Quarto aluno: ')

lista = [alunoUm, alunoDois, alunoTres, alunoQuatro] #Criação de listas de alunos 

escolhido = random.choice(lista) # O escolhido será uma escolha dentro da lista 

print(f'O aluno escolhido foi o {escolhido}')