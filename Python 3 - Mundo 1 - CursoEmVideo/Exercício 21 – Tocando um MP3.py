# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#Importando biblioteca PYGAME
import pygame

#Iniciando a biblioteca PYGAME
pygame.init()
#Comando para carregar a musica no pygame
pygame.mixer.music.load('mario.mp3')
#Rodar a musica
pygame.mixer.music.play()
#Esperar o evento terminar para encerrar o programa
pygame.event.wait()




