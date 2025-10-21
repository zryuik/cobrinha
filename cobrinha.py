import pygame
from pygame.locals import *

import random

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
POS_INICIAL_X = WINDOWS_WIDTH / 2
POS_INICIAL_Y = WINDOWS_HEIGHT / 2
BLOCK = 10


def colisao(pos1,pos2):
    return pos1 == pos2


def verifica_margens(pos):
    if 0 <= pos[0] < WINDOWS_WIDTH and 0 <= pos[1] < WINDOWS_HEIGHT:
        return False
    else:
        return True

def gera_pos_aleatoria():
    x = random.randint(0, WINDOWS_WIDTH)
    y = random.randint(0, WINDOWS_HEIGHT)

    return x // BLOCK * BLOCK , y // BLOCK * BLOCK

def game_over():
    pygame.quit()
    quit()

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))

cobra_pos = [(POS_INICIAL_X,POS_INICIAL_Y),(POS_INICIAL_X + BLOCK,POS_INICIAL_Y),(POS_INICIAL_X + 2 * BLOCK, POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK,BLOCK))
cobra_surface.fill((53,59,72))
direcao = K_LEFT

maca_surface = pygame.Surface((BLOCK,BLOCK))
maca_surface.fill((255,0,0))
maca_pos = gera_pos_aleatoria()


while True:
    pygame.time.Clock().tick(10)
    window.fill((68,189,50))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()

        elif evento.type == KEYDOWN:
            if evento.key in [K_UP,K_DOWN,K_LEFT,K_RIGHT,K_w,K_a,K_s,K_d]:
                direcao = evento.key

    window.blit(maca_surface,maca_pos)   

    if (colisao(cobra_pos[0],maca_pos)):
        cobra_pos.append((-10,-10))
        maca_pos = gera_pos_aleatoria()

    for pos in cobra_pos:
        window.blit(cobra_surface,pos)

    for item in range(len(cobra_pos)- 1, 0, -1):
        cobra_pos[item] = cobra_pos[item-1]

    if verifica_margens(cobra_pos[0]):
        game_over()

    if direcao == K_RIGHT or direcao == K_d:
        cobra_pos[0] = cobra_pos[0][0] + BLOCK,cobra_pos[0][1] #Movimenta para direira

    elif direcao == K_LEFT or direcao == K_a:
        cobra_pos[0] = cobra_pos[0][0] - BLOCK,cobra_pos[0][1] #Movimenta para esquerda

    elif direcao == K_UP or direcao == K_w:
        cobra_pos[0] = cobra_pos[0][0] ,cobra_pos[0][1] - BLOCK #Movimenta para cima

    elif direcao == K_DOWN or direcao == K_s:
        cobra_pos[0] = cobra_pos[0][0] ,cobra_pos[0][1] + BLOCK #Movimenta para baixo
    
    pygame.display.update()
