# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint #Importando a função RANDINT do modulo RANDOM
from time import sleep # função "Sleep" faz com que o PC espere o tempo determinado pelo programador

computador = randint(0, 5) #Computador escolhe um número aleatório
print('*-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('*-' *20)
jogador = input('Em qual número eu pensei? ')
print('Será que você acertou? O.O ')
sleep(2) #Faz o pc esperar 2 segundos antes de mostrar o resultado

if computador == jogador:
    print('Parabens você acertou! ')
else:
    print(f'Você errou o número que pensei foi {computador} e não {jogador}')

