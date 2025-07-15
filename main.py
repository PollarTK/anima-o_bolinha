import pygame
import classes

width = 400
height = 400
loop = True

moving_sprites = pygame.sprite.Group()
player = classes.Player(150,150)
moving_sprites.add(player)

def main():
    pygame.init()

    display = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Animações")

    clock = pygame.time.Clock()
    while loop:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.animate()
    
        display.fill((255,255,255))
        moving_sprites.draw(display)
        moving_sprites.update()
        pygame.display.flip()

main()