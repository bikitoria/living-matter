import pygame
from settings import *
from player import Player
from camera import Camera
from tile import Tile
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        # get the display surface

        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        # camera
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # self.tmx_data = load_pygame("graphics/Sprites/Objects&Tiles/tilemap_1.tmx")
        # for layer in self.tmx_data.visible_layers:
        #     if hasattr(layer, "data"):
        #         for x, y, surf in layer.tiles():
        #             pos = (x * 32, y * 32)
        #             Tile(pos, surf, self.all_sprites)

        self.player = Player((640, 360), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill('white')
        # manually draw all sprites with camera adjustment
        for sprite in self.all_sprites:
            self.display_surface.blit(sprite.image, self.camera.apply(sprite))
        self.all_sprites.update(dt)
        self.camera.update(self.player)