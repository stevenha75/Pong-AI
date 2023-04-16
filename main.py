# A lot of the NEAT implementation was taken from the NEAT documentation below
# https://neat-python.readthedocs.io/en/latest/xor_example.html
from pong import Game
import pygame
import neat
import os
import time
import pickle


class PongGame:
    def __init__(self, window, width, height):
        """
        Initializes the Pong game by creating a new Game object and
        setting up references to its ball and paddles.
        """
        self.game = Game(window, width, height)
        self.ball = self.game.ball
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle


    def test_ai(self, net):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)  # Sets the FPS to 60

            # Update the game state
            game_info = self.game.loop()

            # Check for any events (e.g. quitting the game)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            # Activate the neural network with the current game state as input
            output = net.activate(
                (self.right_paddle.y, abs(self.right_paddle.x - self.ball.x), self.ball.y)
            )

            # Determine which action to take based on the output of the neural network
            decision = output.index(max(output))

            # Move the AI paddle up or down based on the decision
            if decision == 1:  # AI moves up
                self.game.move_paddle(left=False, up=True)
            elif decision == 2:  # AI moves down
                self.game.move_paddle(left=False, up=False)

            # Check for input from the human player to move their paddle
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            elif keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            # Draw the game screen with the current state of the game
            self.game.draw(draw_score=True, draw_hits=False)

            # Update the display to show the new screen
            pygame.display.update()


    def train_ai(self, genome1, genome2, config, draw=False):
        run = True

        # Get the current time in seconds since the start of the program
        start_time = pygame.time.get_ticks() / 1000.0

        # Create the neural networks from the given genomes
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        # Set the genomes to be used later for calculating fitness
        self.genome1 = genome1
        self.genome2 = genome2

        # Set the maximum number of hits before the game ends
        max_hits = 50

        # Start the game loop
        while run:
            # Check for any events (e.g. quitting the game)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

            # Update the game state
            game_info = self.game.loop()

            # Move the AI paddles using the given neural networks
            self.move_ai_paddles(net1, net2)

            # Draw the game screen with the current state of the game
            if draw:
                self.game.draw(draw_score=False, draw_hits=True)

            pygame.display.update()

            # Calculate the duration of the current game
            duration = pygame.time.get_ticks() / 1000.0 - start_time

            # End games early based on the following criterion to speed up training time
            if (
                game_info.left_score == 1
                or game_info.right_score == 1
                or game_info.left_hits >= max_hits
            ):
                # Calculate the fitness of the neural networks based on the results of the game
                self.calculate_fitness(game_info, duration)
                break

        # Return False if the game loop ended normally
        return False

    def move_ai_paddles(self, net1, net2):
        """
        Determine where to move the left and the right paddle based on the two
        neural networks that control them. Punishes the AI if its movement
        causes the paddle to go off the screen.
        """
        players = [
            (self.genome1, net1, self.left_paddle, True),
            (self.genome2, net2, self.right_paddle, False),
        ]
        for genome, net, paddle, left in players:
            output = net.activate((paddle.y, abs(paddle.x - self.ball.x), self.ball.y))
            decision = output.index(max(output))

            valid = True
            if decision == 0:  # Don't move
                genome.fitness -= 0.01  # we want to discourage this
            elif decision == 1:  # Move up
                valid = self.game.move_paddle(left=left, up=True)
            else:  # Move down
                valid = self.game.move_paddle(left=left, up=False)

            if (
                not valid
            ):  # If the movement makes the paddle go off the screen punish the AI
                genome.fitness -= 1

    def calculate_fitness(self, game_info, duration):
        """
        Calculates the fitness of the two genomes based on the game results
        and the duration of the game.
        """
        self.genome1.fitness += game_info.left_hits + duration
        self.genome2.fitness += game_info.right_hits + duration


def eval_genomes(genomes, config):
    # Set the width and height of the game window
    width, height = 700, 500

    # Create the game window and set its caption
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")

    # Iterate over each genome in the population
    for i, (genome_id1, genome1) in enumerate(genomes):
        # Print the progress of the evaluation
        print(round(i / len(genomes) * 100), end=" ")

        # Set the fitness of the current genome to 0
        genome1.fitness = 0

        # Iterate over all remaining genomes in the population
        for genome_id2, genome2 in genomes[min(i + 1, len(genomes) - 1) :]:
            # Set the fitness of the other genome to 0 if it hasn't been set yet
            genome2.fitness = 0 if genome2.fitness is None else genome2.fitness

            # Create a new Pong game with the given genomes and config
            pong = PongGame(win, width, height)

            # Train the two genomes by having them play against each other
            force_quit = pong.train_ai(genome1, genome2, config, draw=True)

            # If the user quits the program during training, quit the program entirely
            if force_quit:
                quit()


def run_neat(config):
    """
    Run the NEAT algorithm using the specified configuration file, and
    save the best genome to a pickle file named "best.pickle".
    """
    # Create a new NEAT population based on the configuration file
    population = neat.Population(config)

    # Add a reporter to print the progress of the algorithm to the console
    population.add_reporter(neat.StdOutReporter(True))

    # Add a reporter to collect statistics on the population and report them to the console
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    # Add a checkpointing reporter to save the current population every 1 generation
    population.add_reporter(neat.Checkpointer(1))

    # Run the NEAT algorithm for 50 generations
    winner = population.run(eval_genomes, 50)

    # Save the best genome to a pickle file
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


def test_best_network(config):
    """
    Load the best genome from the "best.pickle" file, create a neural network
    from it, and test it in a game of Pong.
    """
    # Load the best genome from the pickle file
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)

    # Create a neural network from the best genome
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    # Create a Pong game and test the best network against a human player
    width, height = 700, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")
    pong = PongGame(win, width, height)
    pong.test_ai(winner_net)


if __name__ == "__main__":
    # Get the path to the configuration file
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    # Load the NEAT configuration from the file
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )

    # Run the NEAT algorithm and save the best genome to a file
    # run_neat(config)

    # Load the best genome and test it in a game of Pong
    test_best_network(config)
