import pygame

class Player(pygame.sprite.Sprite):
    NUM_SPRITES = 16

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.contador = 0 
        self.sprites = [pygame.image.load(f"data/bola_{i}.png") for i in range(self.NUM_SPRITES)]
        
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
    
    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_image += 1

            if self.current_image >= len(self.sprites):
                self.current_image = 0
                self.contador += 1

                if self.contador >= 3:
                    self.is_animating = False
                    self.contador = 0

            self.image = self.sprites[self.current_image]
