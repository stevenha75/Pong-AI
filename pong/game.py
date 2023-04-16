from .paddle import Paddle
from .ball import Ball
import pygame
import random

pygame.init()


class GameInformation:
    """
    Initialize instance variables for a GameInformation object
    left_hits: number of hits by the left player
    right_hits: number of hits by the right player
    left_score: score of the left player
    right_score: score of the right player
    """

    def __init__(self, left_hits, right_hits, left_score, right_score):
        self.left_score = left_score
        self.right_score = right_score
        self.left_hits = left_hits
        self.right_hits = right_hits


class Game:
    SCORE_FONT = pygame.font.SysFont("arial", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Initialize instance variables for a game object
    def __init__(self, window, window_width, window_height):
        # Store dimensions of the game window
        self.window_width = window_width
        self.window_height = window_height

        # Create paddles and ball objects
        self.left_paddle = Paddle(10, self.window_height // 2 - Paddle.HEIGHT // 2)
        self.right_paddle = Paddle(
            self.window_width - 10 - Paddle.WIDTH,
            self.window_height // 2 - Paddle.HEIGHT // 2,
        )
        self.ball = Ball(self.window_width // 2, self.window_height // 2)

        # Initialize score and hit counters
        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0

        # Store the Pygame display window
        self.window = window

    def _draw_score(self):
        # Render the left score and right score as text using the SCORE_FONT
        left_score_text = self.SCORE_FONT.render(f"{self.left_score}", 1, self.RED)
        right_score_text = self.SCORE_FONT.render(f"{self.right_score}", 1, self.RED)

        # Blit the left and right score text onto the window,
        # centering them above the middle of the window.
        self.window.blit(
            left_score_text,
            (self.window_width // 4 - left_score_text.get_width() // 2, 20),
        )
        self.window.blit(
            right_score_text,
            (self.window_width * (3 / 4) - right_score_text.get_width() // 2, 20),
        )

    def _draw_hits(self):
        # Calculate the total number of hits
        total_hits = self.left_hits + self.right_hits

        # Render the total number of hits as text using the SCORE_FONT
        hits_text = self.SCORE_FONT.render(f"{total_hits}", 1, self.WHITE)

        # Calculate the x and y positions for the hits text using constants
        HITS_TEXT_X = self.window_width // 2 - hits_text.get_width() // 2
        HITS_TEXT_Y = 10

        # Blit the hits text onto the window at the calculated position
        self.window.blit(hits_text, (HITS_TEXT_X, HITS_TEXT_Y))

    def _draw_divider(self):
        # Calculate the positions for the divider line using a list comprehension
        divider_y_positions = [
            i
            for i in range(10, self.window_height, self.window_height // 20)
            if i % 2 == 0
        ]

        # Calculate the dimensions of the divider line using constants
        DIVIDER_WIDTH = 10
        DIVIDER_HEIGHT = self.window_height // 20

        # Calculate the x position of the divider line using constants and the width of the window
        DIVIDER_X = self.window_width // 2 - DIVIDER_WIDTH // 2

        # Draw the divider line on the window at each y position
        for y in divider_y_positions:
            pygame.draw.rect(
                self.window, self.RED, (DIVIDER_X, y, DIVIDER_WIDTH, DIVIDER_HEIGHT)
            )

    # Handle collisions between the ball and the paddles in a Pong game.
    def _handle_collision(self):
        game_ball = self.ball
        left_paddle_object = self.left_paddle
        right_paddle_object = self.right_paddle

        if game_ball.y + Ball.RADIUS >= self.window_height:
            game_ball.y_vel *= -1
        elif game_ball.y - Ball.RADIUS <= 0:
            game_ball.y_vel *= -1

        if game_ball.x_vel < 0:
            if (
                left_paddle_object.y
                <= game_ball.y
                <= left_paddle_object.y + Paddle.HEIGHT
            ):
                if game_ball.x - Ball.RADIUS <= left_paddle_object.x + Paddle.WIDTH:
                    game_ball.x_vel *= -1

                    middle_y = left_paddle_object.y + Paddle.HEIGHT / 2
                    difference_in_y = middle_y - game_ball.y
                    reduction_factor = (Paddle.HEIGHT / 2) / game_ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    game_ball.y_vel = -1 * y_vel
                    self.left_hits += 1

        else:
            if (
                right_paddle_object.y
                <= game_ball.y
                <= right_paddle_object.y + Paddle.HEIGHT
            ):
                if game_ball.x + Ball.RADIUS >= right_paddle_object.x:
                    game_ball.x_vel *= -1

                    middle_y = right_paddle_object.y + Paddle.HEIGHT / 2
                    difference_in_y = middle_y - game_ball.y
                    reduction_factor = (Paddle.HEIGHT / 2) / game_ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    game_ball.y_vel = -1 * y_vel
                    self.right_hits += 1

    def draw(self, draw_score=True, draw_hits=False):
        """
        Draw the game window with the paddles and ball.

        :param draw_score: whether to draw the score on the screen
        :param draw_hits: whether to draw the hits on the screen
        """
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

        :param left: whether to move the left or right paddle
        :param up: whether to move the paddle up or down
        :returns: boolean indicating if paddle movement is valid.
                  Movement is invalid if it causes paddle to go
                  off the screen.
        """
        paddle = self.left_paddle if left else self.right_paddle
        max_y = self.window_height - Paddle.HEIGHT

        if up:
            if paddle.y - Paddle.VEL < 0:
                return False
            else:
                paddle.move(up)
                return True
        else:
            if paddle.y + Paddle.HEIGHT + Paddle.VEL > self.window_height:
                return False
            else:
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
            left_hits=self.left_hits,
            right_hits=self.right_hits,
            left_score=self.left_score,
            right_score=self.right_score,
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
