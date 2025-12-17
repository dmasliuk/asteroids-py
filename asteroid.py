import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from random import uniform

class Asteroid(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(
      screen,
      "#FFFFFF",
      self.position,
      self.radius,
      LINE_WIDTH
    )
  
  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    log_event("asteroid_split")
    angle = uniform(20, 50)
    new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
    first_asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
    second_asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
    first_asteroid.velocity = self.velocity.rotate(angle) * 1.2
    second_asteroid.velocity = self.velocity.rotate(-angle) * 1.2