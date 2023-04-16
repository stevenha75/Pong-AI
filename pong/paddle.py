import pygame


class Paddle:
    VEL = 4
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, x, y):
        """
        Initializes the Paddle object.

        :param x: X coordinate of the paddle.
        :param y: Y coordinate of the paddle.
        """
        self.x = self.original_x = x
        self.y = self.original_y = y

    def draw(self, win):
        """
        Draws the Paddle object on the given window.

        :param win: The window to draw on.
        """
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.WIDTH, self.HEIGHT))

    def move(self, up=True):
        """
        Moves the Paddle object up or down.

        :param up: A boolean value. True to move up, False to move down.
        """
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        """Resets the Paddle object to its original position."""
        self.x = self.original_x
        self.y = self.original_y
