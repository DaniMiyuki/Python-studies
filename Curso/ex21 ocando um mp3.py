# faca um programa em python que abra e reproduza o audio de u arquivo mp3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('unha.mp3')
pygame.mixer.music.play()
pygame.event.wait()
