import pygame
import math
import random


class Ball:
    MAX_VEL = 5
    RADIUS = 10

    def __init__(self, x, y):
        # Store initial position values as original position values
        self.x = self.original_x = x
        self.y = self.original_y = y

        # Get a random angle between -30 and 30 degrees
        # Convert the angle to radians, and calculate x and y velocities
        angle = self._get_random_angle(-30, 30, [0])
        pos = 1 if random.random() < 0.5 else -1
        self.x_vel = pos * abs(math.cos(angle) * self.MAX_VEL)
        self.y_vel = math.sin(angle) * self.MAX_VEL

    def _get_random_angle(self, min_angle, max_angle, excluded):
        angle = 0
        while angle in excluded:
            # Generate a random angle within the given range in degrees,
            # convert it to radians, and check if it is in the excluded list
            angle = math.radians(random.randrange(min_angle, max_angle))

        return angle

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.RADIUS)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        # Reset object to its original position
        self.x = self.original_x
        self.y = self.original_y

        # Calculate new velocities based on a random angle
        angle = self._get_random_angle(-30, 30, [0])
        x_vel = abs(math.cos(angle) * self.MAX_VEL)
        y_vel = math.sin(angle) * self.MAX_VEL

        # Assign new velocities to the object
        self.y_vel = y_vel
        self.x_vel = -x_vel
