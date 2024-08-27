import pygame
from settings import *
# from support import *
from timer import Timer
import spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)  # Corrected this line
        self.import_assets()
        self.status = 'down'
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        # timers
        self.timers = {

        }

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def import_assets(self):
        sprite_sheet_up_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_up.png').convert_alpha()
        sprite_sheet_up = spritesheet.SpriteSheet(sprite_sheet_up_image)

        sprite_sheet_down_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_down.png').convert_alpha()
        sprite_sheet_down = spritesheet.SpriteSheet(sprite_sheet_down_image)

        sprite_sheet_left_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_left.png').convert_alpha()
        sprite_sheet_left = spritesheet.SpriteSheet(sprite_sheet_left_image)

        sprite_sheet_right_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_right.png').convert_alpha()
        sprite_sheet_right = spritesheet.SpriteSheet(sprite_sheet_right_image)

        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': []}

        for animation in self.animations.keys():
            if animation == 'up':
                for i in range(int(sprite_sheet_up_image.get_width() / 32)):
                    self.animations[animation] += sprite_sheet_up.get_image(i, 24, 24, 3, (0, 0, 0))

    def update(self, dt):
        #self.input()
        #self.move(dt)
        #self.get_status()
        #self.update_timers()
        self.animate(dt)