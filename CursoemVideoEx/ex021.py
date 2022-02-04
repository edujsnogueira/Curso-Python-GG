# Exercício 021:

# Faça um programa em Python que abra e repoduza um áudio de um arquivo de mp3.

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

# Existem outros módulos que fazem o mesmo trabalho:
'''from playsound import playsound
playsound('ex021.mp3')'''
