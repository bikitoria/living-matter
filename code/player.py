import pygame
from core.entity import Entity, MovementState


class Player(Entity):

    DIRECTIONS = [
        (pygame.K_w, pygame.Vector2(0, -1), MovementState.UP),
        (pygame.K_s, pygame.Vector2(0, 1), MovementState.DOWN),
        (pygame.K_a, pygame.Vector2(-1, 0), MovementState.LEFT),
        (pygame.K_d, pygame.Vector2(1, 0), MovementState.RIGHT),
    ]

    def __init__(self, pos: pygame.Vector2, group: pygame.sprite.Group):
        super().__init__(
            pos,
            group,
            {
                "up_idle": "graphics/Sprites/Zombie/Zombie_up_idle.png",
                "up": "graphics/Sprites/Zombie/Zombie_up.png",
                "down_idle": "graphics/Sprites/Zombie/Zombie_down_idle.png",
                "down": "graphics/Sprites/Zombie/Zombie_down.png",
                "left_idle": "graphics/Sprites/Zombie/Zombie_left_idle.png",
                "left": "graphics/Sprites/Zombie/Zombie_left.png",
                "right_idle": "graphics/Sprites/Zombie/Zombie_right_idle.png",
                "right": "graphics/Sprites/Zombie/Zombie_right.png",
            },
        )

    def input(self):
        keys = pygame.key.get_pressed()
        result_direction: pygame.Vector2 = self.direction
        result_state: MovementState = self.movement_state
        result_direction.x = 0
        result_direction.y = 0
        for data in self.DIRECTIONS:
            if keys[data[0]]:
                result_direction.x += data[1].x
                result_direction.y += data[1].y
                result_state = data[2]
        self.movement_state = result_state
        self.direction = result_direction

    def update(self, dt) -> None:
        self.input()
        return super().update(dt)
