import pygame
def moveTick(pos,velo):
    if event.key == pygame.KEYDOWN
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            velo[0]=-20
            pos[0]+=velo[0]
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            velo[0]=20
            pos[0]+=velo[0]
        if onGround():
            if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                velo[1]=25
                pos[1]+=velo[1]
        else:
            velo[1]-=5
            pos[1]+=velo[1]
    elif event.key == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            velo[0]=0
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            velo[0]=0
    return pos,velo
def onGround():
    return true