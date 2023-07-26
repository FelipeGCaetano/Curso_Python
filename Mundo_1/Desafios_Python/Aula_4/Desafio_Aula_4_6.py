#Faça um programa python que abra e reproduza um áudio de um arquivo mp3

import pygame   
pygame.mixer.init()
pygame.mixer.music.load('enemy.mp3')
pygame.mixer.music.play()

