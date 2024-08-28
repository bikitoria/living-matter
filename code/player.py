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
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def import_assets(self):
        animation_paths = {
            'up_idle': 'graphics/Sprites/Zombie/Zombie_up_idle.png',
            'up': 'graphics/Sprites/Zombie/Zombie_up.png',
            'down_idle': 'graphics/Sprites/Zombie/Zombie_down_idle.png',
            'down': 'graphics/Sprites/Zombie/Zombie_down.png',
            'left_idle': 'graphics/Sprites/Zombie/Zombie_left_idle.png',
            'left': 'graphics/Sprites/Zombie/Zombie_left.png',
            'right_idle': 'graphics/Sprites/Zombie/Zombie_right_idle.png',
            'right': 'graphics/Sprites/Zombie/Zombie_right.png',
        }

        self.animations = {
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
            'up': [], 'down': [], 'left': [], 'right': []}

        for animation in self.animations.keys():
            temp = []
            sprite_sheet_image = pygame.image.load(animation_paths[animation]).convert_alpha()
            sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
            for i in range(int(sprite_sheet_image.get_width() / 32)):
                temp.append(sprite_sheet.get_image(i, 32, 32, 3, (0, 0, 0)))
            self.animations[animation] = temp

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def move(self, dt):

        # normalizing a vector / makiing sure the direction fo the vector is always 1
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

    def update(self, dt):
        self.input()
        self.move(dt)
        self.get_status()
        # self.update_timers()
        self.animate(dt)
