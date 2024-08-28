import pygame
import numpy as np

class Tilemap(pygame.sprite.Sprite):
    def __init__(self, tileset, group, size=(10, 20)):
        super().__init__(group)
        self.size = size
        self.tileset = tileset
        self.tilewidth = tileset.size[0]
        self.tileheight = tileset.size[1]
        self.map = np.zeros(size, dtype=int)

        h, w = self.size
        self.image = pygame.Surface((self.tilewidth*w, self.tileheight*h))
        self.rect = self.image.get_rect()
    
    def set(self, array):
        self.map = np.array(array, dtype=int)
        self.render()

    def render(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (j*self.tilewidth, i*self.tileheight))

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'
