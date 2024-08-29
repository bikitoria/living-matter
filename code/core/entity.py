import core.spritesheet as spritesheet
import pygame
from enum import Enum


def import_animation_assets(self: "Entity", anim_paths: dict[str, str]):
    """
    Imports the animations for the entity given a dictionary of animation names to paths

    Parameters
    ----------
    anim_paths : dict[str, str]
        A dictionary of animation names to paths
    """
    animations = {k: [] for k in MovementState}
    for anim_state, l in animations.items():
        sprite_sheet_image: pygame.Surface = pygame.image.load(
            anim_paths[str(anim_state)]
        ).convert_alpha()
        sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
        for i in range(int(sprite_sheet_image.get_width() / 32)):
            l.append(sprite_sheet.get_image(i, 32, 32, 3, (0, 0, 0)))
    self.animations = animations


class MovementState(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_IDLE = 5
    DOWN_IDLE = 6
    LEFT_IDLE = 7
    RIGHT_IDLE = 8

    def __str__(self) -> str:
        return self.name.lower()

    def get_idle(self) -> "MovementState":
        match self:
            case MovementState.UP:
                return MovementState.UP_IDLE
            case MovementState.DOWN:
                return MovementState.DOWN_IDLE
            case MovementState.LEFT:
                return MovementState.LEFT_IDLE
            case MovementState.RIGHT:
                return MovementState.RIGHT_IDLE
        return self


class Entity(pygame.sprite.Sprite):

    movement_state: MovementState = MovementState.DOWN
    rect: pygame.Rect
    image: pygame.Surface
    position: (
        pygame.Vector2
    )  # Don't set this directly, it wont update the rect's position
    direction: pygame.Vector2
    speed: int = 200
    frame_index: int = 0
    animation_speed: int = 10
    animations: dict[MovementState, list[pygame.Surface]]

    def __init__(
        self,
        starter_pos: pygame.Vector2,
        group: pygame.sprite.Group,
        anim_paths: dict[str, str],
    ) -> None:
        super().__init__(group)
        import_animation_assets(self, anim_paths)
        self.image = self.animations[self.movement_state][self.frame_index]
        self.rect = self.image.get_rect(center=starter_pos)
        self.direction = pygame.Vector2()
        self.position = starter_pos

    def move_to(self, pos: pygame.Vector2):
        """
        Move the entity to the given position.

        :param pos: The new position of the entity.
        :type pos: math.Vector2
        """
        self.position = pos
        self.rect.center = pos

    def move(self, dt: float):
        """
        Move the entity by the given amount.

        :param dt: The amount to move the entity, in seconds.
        :type dt: float
        """
        # normalizing a vector / makiing sure the direction fo the vector is always 1
        if self.direction.magnitude() > 1:
            self.direction = self.direction.normalize()
        self.move_to(self.position + self.direction * self.speed * dt)

    def update_movement_state(self):
        """
        Update the movement state to the idle state if the direction is zero.
        """
        if self.direction.magnitude() == 0:
            self.movement_state = self.movement_state.get_idle()

    def animate(self, dt: float):
        """
        Animate the entity based on the movement state and the animation speed.

        Args:
            dt (float): The delta time.
        """
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.animations[self.movement_state]):
            self.frame_index = 0
        self.image = self.animations[self.movement_state][int(self.frame_index)]

    def update(self, dt) -> None:
        """
        Update the entity's position, movement state and animation.

        Args:
            dt (float): The delta time.
        """
        self.move(dt)
        self.update_movement_state()
        self.animate(dt)
