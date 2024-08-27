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
        print(len(self.animations[self.status]))
        self.image = self.animations[self.status][int(self.frame_index)]

    def import_assets(self):
        sprite_sheet_up_idle_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_up_idle.png').convert_alpha()
        sprite_sheet_up_idle = spritesheet.SpriteSheet(sprite_sheet_up_idle_image)
        sprite_sheet_up_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_up.png').convert_alpha()
        sprite_sheet_up = spritesheet.SpriteSheet(sprite_sheet_up_image)

        sprite_sheet_down_idle_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_down_idle.png').convert_alpha()
        sprite_sheet_down_idle_ = spritesheet.SpriteSheet(sprite_sheet_down_idle_image)
        sprite_sheet_down_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_down.png').convert_alpha()
        sprite_sheet_down = spritesheet.SpriteSheet(sprite_sheet_down_image)

        sprite_sheet_left_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_left.png').convert_alpha()
        sprite_sheet_left = spritesheet.SpriteSheet(sprite_sheet_left_image)
        sprite_sheet_left_idle_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_left_idle.png').convert_alpha()
        sprite_sheet_left_idle = spritesheet.SpriteSheet(sprite_sheet_left_idle_image)

        sprite_sheet_right_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_right.png').convert_alpha()
        sprite_sheet_right = spritesheet.SpriteSheet(sprite_sheet_right_image)
        sprite_sheet_right_idle_image = pygame.image.load('graphics/Sprites/Zombie/Zombie_right_idle.png').convert_alpha()
        sprite_sheet_right_idle = spritesheet.SpriteSheet(sprite_sheet_right_idle_image)

        self.animations = {
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
            'up': [], 'down': [], 'left': [], 'right': []}

        for animation in self.animations.keys():
            if animation == 'up_idle':
                temp = []
                for i in range(int(sprite_sheet_up_idle_image.get_width() / 32)):
                    temp.append(sprite_sheet_up_idle.get_image(i, 32, 32, 3, (0, 0, 0)))
                self.animations[animation] = temp
            if animation == 'up':
                temp = []
                for i in range(int(sprite_sheet_up_image.get_width() / 32)):
                    temp.append(sprite_sheet_up.get_image(i, 32, 32, 3, (0, 0, 0)))
                self.animations[animation] = temp

            if animation == 'down_idle':
                temp = []
                for i in range(int(sprite_sheet_down_idle_image.get_width() / 32)):
                    temp.append(sprite_sheet_down_idle_.get_image(i, 32, 32, 3, (0, 0, 0)))
                self.animations[animation] = temp
            if animation == 'down':
                temp = []
                for i in range(int(sprite_sheet_down_image.get_width() / 32)):
                    temp.append(sprite_sheet_down.get_image(i, 32, 32, 3, (0, 0, 0)))
                self.animations[animation] = temp

            if animation == 'left':
                temp = []
                for i in range(int(sprite_sheet_left_image.get_width() / 32)):
                    temp.append(sprite_sheet_left.get_image(i, 32, 32, 3, (0, 0, 0)))
                self.animations[animation] = temp
            if animation == 'left_idle':
                temp = []
                for i in range(int(sprite_sheet_left_idle_image.get_width() / 32)):
                    temp.append(sprite_sheet_left_idle.get_image(i, 32, 32, 3, (0, 0, 0)))
                self.animations[animation] = temp

            if animation == 'right':
                temp = []
                for i in range(int(sprite_sheet_right_image.get_width() / 32)):
                    temp.append(sprite_sheet_right.get_image(i, 32, 32, 3, (0, 0, 0)))
                self.animations[animation] = temp
            if animation == 'right_idle':
                temp = []
                for i in range(int(sprite_sheet_right_idle_image.get_width() / 32)):
                    temp.append(sprite_sheet_right_idle.get_image(i, 32, 32, 3, (0, 0, 0)))
                self.animations[animation] = temp

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
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
