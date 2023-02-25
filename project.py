import pygame

pygame.init()

# Creating window
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Pong by Steven Ha")

# Global constants
FPS = 60
RED = (237, 64, 64)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 10
SCORE_FONT = pygame.font.SysFont("arial", 50)


class Paddle:
    # Class constants
    COLOR = RED
    VEL = 4

    # Paddle Constructor
    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    # Class constants
    MAX_VEL = 5
    COLOR = RED

    # Ball constructor
    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)

    # Storing score text
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, RED)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, RED)

    # Rendering score text
    win.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    win.blit(
        right_score_text, (WIDTH * (3 / 4) - right_score_text.get_width() // 2, 20)
    )

    # Drawing each paddle
    for paddle in paddles:
        paddle.draw(win)

    # Drawing dotted line in the center
    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, RED, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    ball.draw(win)

    pygame.display.update()


# Shortened w/ ChatGPT
def handle_collision(ball, left_paddle, right_paddle):
    # Handling ceiling and floor collision
    if ball.y + ball.radius >= HEIGHT or ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    # Handling paddle collision
    if (
        ball.x_vel < 0
        and ball.x - ball.radius <= left_paddle.x + left_paddle.width
        and left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height
    ):
        ball.x_vel *= -1
        ball.y_vel = (
            (ball.y - (left_paddle.y + left_paddle.height / 2))
            / (left_paddle.height / 2)
            * -ball.MAX_VEL
        )
    elif (
        ball.x_vel > 0
        and ball.x + ball.radius >= right_paddle.x
        and right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height
    ):
        ball.x_vel *= -1
        ball.y_vel = (
            (ball.y - (right_paddle.y + right_paddle.height / 2))
            / (right_paddle.height / 2)
            * -ball.MAX_VEL
        )


# Shortened w/ ChatGPT
def check_paddle_movement(keys, left_paddle, right_paddle):
    # Left paddle movement (W & S)
    if keys[pygame.K_w]:
        left_paddle.move(up=True)
    elif keys[pygame.K_s]:
        left_paddle.move(up=False)

    # Right paddle movement (Arrow keys: UP & DOWN)
    if keys[pygame.K_UP]:
        right_paddle.move(up=True)
    elif keys[pygame.K_DOWN]:
        right_paddle.move(up=False)

    # Keep paddles within screen boundaries
    left_paddle.y = max(0, min(left_paddle.y, HEIGHT - left_paddle.height))
    right_paddle.y = max(0, min(right_paddle.y, HEIGHT - right_paddle.height))


def reset_all(ball, left_paddle, right_paddle):
    ball.reset()
    left_paddle.reset()
    right_paddle.reset()


def check_win(left_score, right_score):
    won = False
    win_text = ""
    if left_score >= 15:
        won = True
        win_text = "Left Player Won!"
    elif right_score >= 15:
        won = True
        win_text = "Right Player Won!"
    return won, win_text


# Checks whether each player scores and allocates points
def handle_score(ball, left_paddle, right_paddle, left_score, right_score):
    # Store temp values
    temp_right_score = right_score
    temp_left_score = left_score

    # Modify accordingly
    if ball.x < 0:
        temp_right_score = right_score + 1
        reset_all(ball, left_paddle, right_paddle)
    elif ball.x > WIDTH:
        temp_left_score = left_score + 1
        reset_all(ball, left_paddle, right_paddle)

    # Returning modified scores
    return temp_left_score, temp_right_score


def main():
    run = True
    left_score = 0
    right_score = 0

    # Initializing Objects
    clock = pygame.time.Clock()
    left_paddle = Paddle(
        10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
    )
    right_paddle = Paddle(
        WIDTH - 10 - PADDLE_WIDTH,
        HEIGHT // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    while run:
        # Regulates speed of while loop to 60 FPS
        clock.tick(FPS)

        # Draws all elements in the window WIN
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        # Checks for the window closing -> ends loop if condition met
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Handling paddle movement
        keys = pygame.key.get_pressed()
        check_paddle_movement(keys, left_paddle, right_paddle)

        # Handling ball movement
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        # Handling score counter
        left_score, right_score = handle_score(
            ball, left_paddle, right_paddle, left_score, right_score
        )

        # Winning screen
        won, win_text = check_win(left_score, right_score)
        if won:
            text = SCORE_FONT.render(win_text, 1, RED)
            WIN.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    HEIGHT // 2 - text.get_height() // 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(5000)
            reset_all(ball, left_paddle, right_paddle)
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == "__main__":
    main()
