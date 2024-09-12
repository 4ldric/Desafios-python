# FAÇA UM PROGRAMA QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3

# precisamos realizar a instalação dos package do modulo ( python -m pip install pygame)

import pygame
pygame.init() # INICIALIZANDO O MODULO

pygame.mixer.music.load('desafio020.mp3') # ESCOLHNDO O ArQUIVO
pygame.mixer.music.play() #inicializando arquivo
pygame.event.wait() # definindo a parada apos o programa ser encerrado