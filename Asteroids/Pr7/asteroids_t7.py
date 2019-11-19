#!/usr/bin/env python

import math
import random
import pygame
from pygame.locals import *


class World(object):
    """ contains all of our game state """

    RENDER_OPTIONS = HWSURFACE | DOUBLEBUF | RESIZABLE
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, size, player):
        # setting up the screen
        self.size = size
        self.surface = pygame.display.set_mode(size, self.RENDER_OPTIONS)
        self.surface.fill(self.BLACK)

        # stash the player sprite
        self.player = player

        # adding a sprite group
        self.sprites = pygame.sprite.RenderUpdates()
        self.sprites.add(player)

        # setup our event handlers
        self.event_handlers = {
            VIDEORESIZE: self.handle_resize,
            #KEYDOWN: self.handle_keydown,
            #KEYUP: self.handle_keyup
        }

    def update(self):
        # allow any sprites to update themselves
        self.sprites.update()

        # change the sprite's location to match it's proper motion
        for sprite in self.sprites:
            # grab the next position the sprite should be at
            new_center = Vector.from_position(sprite.rect.center) + sprite.motion
            new_center = new_center.to_position()

            # do the screen wrap for the x and y positions
            x = new_center[0] % self.size[0]
            y = new_center[1] % self.size[1]
            sprite.rect.center = (x, y)

    def render(self):
        """ render the sprites to the window """
        def clear_callback(surface, rect):
            surface.fill(self.BLACK, rect)

        self.sprites.clear(self.surface, clear_callback)
        updatedRects = self.sprites.draw(self.surface)
        pygame.display.update(updatedRects)

    def handle_event(self, event):
        handler = self.event_handlers.get(event.type, lambda x: None)
        handler(event)

    def handle_resize(self, event):
        """ set the window size """
        self.size = event.dict['size']
        self.surface = pygame.display.set_mode(self.size, self.RENDER_OPTIONS)


class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        """ return the magnitude (aka: distance) this vector represents """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        """ return a unit vector """
        return self / self.magnitude()

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, n):
        x = self.x * n
        y = self.y * n
        return Vector(x, y)

    def __div__(self, n):
        x = self.x / n
        y = self.y / n
        return Vector(x, y)

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def to_position(self):
        return (self.x, self.y)

    def to_radians(self):
        radians = math.atan2(self.x, self.y)
        return (radians, self.magnitude())

    def to_degrees(self):
        radians, magnitude = self.to_radians()
        return (math.degrees(radians), magnitude)

    @classmethod
    def from_position(self, position):
        return Vector(position[0], position[1])

    @classmethod
    def from_radians(self, radians, magnitude=1):
        return Vector(math.sin(radians), math.cos(radians)) * magnitude

    @classmethod
    def from_degrees(self, degrees, magnitude=1):
        return Vector.from_radians(math.radians(degrees), magnitude)


class Entity(pygame.sprite.Sprite):

    def __init__(self, image, position):
        super(Entity, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.motion = Vector(0, 0)


class Player(Entity):
    """ represents the player """

    def __init__(self, position):
        self.orig_image = pygame.image.load('assets/ship.png')
        super(Player, self).__init__(self.orig_image, position)
        self.position = position
        self.facing = Vector.from_degrees(90)
        self.forward = False
        self.backward = False
        self.turn_left = False
        self.turn_right = False
        self.accel = 0.15

    def update(self):
        # if we are thrusting, add the vector of our facing to the motion
        if self.forward:
            self.motion = self.motion - self.facing * self.accel

        if self.backward:
            self.motion = self.motion + self.facing * self.accel

        degrees, _ = self.facing.to_degrees()
        if self.turn_left:
            degrees = (degrees + 10) % 360

        if self.turn_right:
            degrees = (degrees - 10) % 360

        self.facing = Vector.from_degrees(degrees)

        # rotate our sprite to match our direction, and put it in the right place
        current = self.rect.center
        self.image = pygame.transform.rotate(self.orig_image, degrees)
        self.rect = self.image.get_rect()
        self.rect.center = current

class Asteroid(Entity):
    def __init__(self, position):
        self.orig_image = pygame.image.load('assets/asteroid.png')
        self.duration = 1000
        super(Asteroid, self).__init__(self.orig_image, position)
        self.motion = Vector(random.randint(-3,3), random.randint(-3,3))

    def update(self):
        if self.duration == 0:
            self.kill()

        self.duration-=5
        
class Bullet(Entity):
    def __init__(self, position,direction,magnitude):
        self.orig_image = pygame.image.load('assets/bullet.png')
        self.duration = 1000
        super(Bullet, self).__init__(self.orig_image, position)
        self.position = position
        self.motion = Vector.from_degrees(direction, magnitude)
    def update(self):
        if self.duration == 0:
            self.kill()

        self.duration-=5


def main():
    """ runs our application """
    # setup pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption("Asteroids 0.2")

    # store our game state
    player = Player((400, 300))
    world = World((800, 600), player)
    world.pew = pygame.mixer.Sound('assets/pew.wav')
    bullet = Bullet((world.player.position),20.0,20)

    # use the clock to throttle the fps to something reasonable
    clock = pygame.time.Clock()

    # main loop

    running = True
    tope = 29
    i = 0
    f = 40

    while running:
        if f%40 == 0 and i < tope:
            asteroid = Asteroid((random.randint(1,900),random.randint(1,900)))
            events = pygame.event.get()
            world.sprites.add(asteroid)
            f = 40
            i += 1
        events = pygame.event.get()
        world.sprites.add(bullet)

        # handle our events
        for event in events:
            if event.type == QUIT:
                running = False
                break

            world.handle_event(event)

        world.update()
        world.render()
        clock.tick(40)
        pygame.display.flip()
        f -= 1

if __name__ == "__main__":
    main()
