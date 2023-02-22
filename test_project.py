# 3 Tests are required (all functions tested must be defined at the same indentation level as main)
# Naming: test_custom_function where custom_function is implemented in project.py

from project import Paddle, Ball, reset_all, check_win, handle_score

# Global Constants
WIDTH, HEIGHT = 700, 500
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 10


def test_reset_all():
    # Initializing all objects
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

    # Set position values
    ball.x = 500
    ball.y = 500
    right_paddle.x = 500
    right_paddle.y = 500
    left_paddle.x = 500
    left_paddle.y = 500

    # Reset position
    reset_all(ball, left_paddle, right_paddle)

    # Check positions have been reset
    assert ball.x == 350
    assert ball.y == 250
    assert right_paddle.x == 670
    assert right_paddle.y == 200
    assert left_paddle.x == 10
    assert right_paddle.y == 200


# Checking False case of check_win() method
def test_check_win_false():
    left_score = 10
    right_score = 10
    won, win_text = check_win(left_score, right_score)
    assert won == False
    assert win_text == ""


# Checking True case of check_win() method
def test_check_win_true():
    left_score = 16
    right_score = 5
    won, win_text = check_win(left_score, right_score)
    assert won == True
    assert win_text == "Left Player Won!"
    

def test_handle_score():
    # Initializing score
    left_score = 0
    right_score = 0
    
    # Initializing Objects
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
    
    # Reassinging score
    left_score, right_score = handle_score(ball, left_paddle, right_paddle, left_score, right_score)
    
    # Checking for the correct score
    assert left_score == ...
    assert right_score == ...