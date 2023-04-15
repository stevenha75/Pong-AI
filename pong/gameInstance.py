from .paddle import Paddle
from .ball import Ball
import pygame
import random

pygame.init()


class GameInformation:
    def __init__(self, left_hits, right_hits, left_score, right_score):
        self.left_hits = left_hits
        self.right_hits = right_hits
        self.left_score = left_score
        self.right_score = right_score


class Game:
    SCORE_FONT = pygame.font.SysFont("arial", 50)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, window, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.left_paddle = Paddle(10, self.window_height // 2 - Paddle.HEIGHT // 2)
        self.right_paddle = Paddle(
            self.window_width - 10 - Paddle.WIDTH,
            self.window_height // 2 - Paddle.HEIGHT // 2,
        )
        self.ball = Ball(self.window_width // 2, self.window_height // 2)

        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0
        self.window = window

    def _draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.window.blit(text_surface, text_rect)

    def _draw_score(self):
        self._draw_text(
            f"{self.left_score}",
            self.SCORE_FONT,
            self.RED,
            self.window_width // 4,
            20,
        )
        self._draw_text(
            f"{self.right_score}",
            self.SCORE_FONT,
            self.RED,
            self.window_width * (3 / 4),
            20,
        )

    def _draw_hits(self):
        self._draw_text(
            f"{self.left_hits + self.right_hits}",
            self.SCORE_FONT,
            self.RED,
            self.window_width // 2,
            10,
        )

    def _draw_divider(self):
        for i in range(10, self.window_height, self.window_height // 20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(
                self.window,
                self.RED,
                (self.window_width // 2 - 5, i, 10, self.window_height // 20),
            )

    def _handle_collision(self):
        ball = self.ball
        left_paddle = self.left_paddle
        right_paddle = self.right_paddle

        # Vertical collision detection and handling
        if ball.y + ball.RADIUS >= self.window_height or ball.y - ball.RADIUS <= 0:
            ball.y_vel *= -1

        # Horizontal collision detection and handling
        if ball.x_vel < 0 and ball.x - ball.RADIUS <= left_paddle.x + Paddle.WIDTH:
            if left_paddle.y <= ball.y <= left_paddle.y + Paddle.HEIGHT:
                ball.x_vel *= -1

                middle_y = left_paddle.y + Paddle.HEIGHT / 2
                difference_in_y = middle_y - ball.y
                ball.y_vel = -difference_in_y / ((Paddle.HEIGHT / 2) / ball.MAX_VEL)
                self.left_hits += 1

        elif ball.x_vel > 0 and ball.x + ball.RADIUS >= right_paddle.x:
            if right_paddle.y <= ball.y <= right_paddle.y + Paddle.HEIGHT:
                ball.x_vel *= -1

                middle_y = right_paddle.y + Paddle.HEIGHT / 2
                difference_in_y = middle_y - ball.y
                ball.y_vel = -difference_in_y / ((Paddle.HEIGHT / 2) / ball.MAX_VEL)
                self.right_hits += 1

    def draw(self, draw_score=True, draw_hits=False):
        self.window.fill(self.BLACK)

        self._draw_divider()

        if draw_score:
            self._draw_score()

        if draw_hits:
            self._draw_hits()

        for paddle in [self.left_paddle, self.right_paddle]:
            paddle.draw(self.window)

        self.ball.draw(self.window)

    def move_paddle(self, left=True, up=True):
        """
        Move the left or right paddle.

        :returns: boolean indicating if paddle movement is valid.
                Movement is invalid if it causes paddle to go
                off the screen
        """
        paddle = self.left_paddle if left else self.right_paddle

        if up and paddle.y - Paddle.VEL < 0:
            return False
        if not up and paddle.y + Paddle.HEIGHT > self.window_height:
            return False

        paddle.move(up)
        return True

    def loop(self):
        """
        Executes a single game loop.

        :returns: GameInformation instance stating score
                and hits of each paddle.
        """
        self.ball.move()
        self._handle_collision()

        if self.ball.x < 0:
            self.right_score += 1
            self.ball.reset()
        elif self.ball.x > self.window_width:
            self.left_score += 1
            self.ball.reset()


        game_info = GameInformation(
            self.left_hits, self.right_hits, self.left_score, self.right_score
        )

        return game_info

    def reset(self):
        """Resets the entire game."""
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0
