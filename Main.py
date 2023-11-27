import random #for number
import sys
import pygame 
from pygame.locals import *

FPS = 32
SCREENWIDTH = 289
SCREENHIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHIGHT))
GROUNDY = SCREENHIGHT * 0.8
GAME_SPRITES ={}
GAME_SOUNDS ={}
PLAYER = ""
BACKGROUND = ""
PIPE = ""


if __name__ == "__main__":

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("|Flappy Bird")
    GAME_SPRITES["numbers"] = (
        pygame.image.load(".png").convert_alpha(),
        pygame.image.load(".png").convert_alpha(),
        pygame.image.load(".png").convert_alpha(),
        pygame.image.load(".png").convert_alpha(),
        pygame.image.load(".png").convert_alpha(),
        pygame.image.load(".png").convert_alpha(),
        pygame.image.load(".png").convert_alpha(),
        pygame.image.load(".png").convert_alpha(),
        pygame.image.load(".png").convert_alpha(),
    )





    