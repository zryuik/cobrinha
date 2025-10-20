import pygame
from pygame.locals import *
##
WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
POS_INICIAL_X = WINDOWS_WIDTH / 2
POS_INICIAL_Y = WINDOWS_HEIGHT / 2
BLOCK = 10

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))

cobra_pos = [(POS_INICIAL_X,POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK,BLOCK))
cobra_surface.fill((53,59,72))
direcao = K_LEFT

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
    for pos in cobra_pos:
        window.blit(cobra_surface,pos)

    if direcao == K_RIGHT or direcao == K_d:
        cobra_pos[0] = cobra_pos[0][0] + BLOCK,cobra_pos[0][1] #Movimenta para direira

    elif direcao == K_LEFT or direcao == K_a:
        cobra_pos[0] = cobra_pos[0][0] - BLOCK,cobra_pos[0][1] #Movimenta para esquerda

    elif direcao == K_UP or direcao == K_w:
        cobra_pos[0] = cobra_pos[0][0] ,cobra_pos[0][1] - BLOCK #Movimenta para cima

    elif direcao == K_DOWN or direcao == K_s:
        cobra_pos[0] = cobra_pos[0][0] ,cobra_pos[0][1] + BLOCK #Movimenta para baixo
    
    pygame.display.update()
