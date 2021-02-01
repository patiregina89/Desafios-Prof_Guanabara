'''Faça um programa no python que abra e reproduza o áudio de arquivo em MP3'''

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3') # nao vai funcionar pq nao baixei a musica ;)
pygame.mixer.music.play
pygame.event.wait()

