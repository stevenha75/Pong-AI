# Pong AI - CS50P Final Project
 Recreation of Pong that utilizes NEAT, a machine learning algorithm. 

## Table of Contents
- [Task List](https://github.com/stevenha75/Pong-AI#task-list)
- [Video Demo](https://github.com/stevenha75/Pong-AI#video-demo)
- [Installation & Usage](https://github.com/stevenha75/Pong-AI#installation--usage)
  - [Dependencies](https://github.com/stevenha75/Pong-AI#dependencies)
  - [Installation](https://github.com/stevenha75/Pong-AI#installation)
  - [Controls](https://github.com/stevenha75/Pong-AI#controls)
  - [Using the AI](https://github.com/stevenha75/Pong-AI#using-the-ai)
- [How It Works](https://github.com/stevenha75/Pong-AI#how-it-works)
  - [Pong Game Overview](https://github.com/stevenha75/Pong-AI#pong-game-overview)
    - Collision
  - [AI Overview](https://github.com/stevenha75/Pong-AI/blob/main/README.md#ai-overview)
- [Post-project reflection](https://github.com/stevenha75/Pong-AI/edit/main/README.md#post-project-reflection)

## Task List
 - [ ] Add testing
 - [ ] Create a main menu screen

 ## Video Demo
 - This video is outdated and does not include AI implementation

[![CS50P Final Project Demo](http://img.youtube.com/vi/TM2VOzjg8Xg/0.jpg)](https://www.youtube.com/watch?v=TM2VOzjg8Xg)

 # Installation & Usage

   ## Dependencies
 - [Pygame](https://www.pygame.org/wiki/GettingStarted)
 - [Python](https://www.python.org/downloads/)
 - [neat-python](https://neat-python.readthedocs.io/en/latest/installation.html)

 ## Installation
 1. First clone the repository\
 ```git clone https://github.com/stevenha75/kickproxies/git```
 2. Install dependencies then run main.py (this will put you in a game vs. an AI. This AI was not trained for many generations and has very poor performance). For further explanation on how to train a better AI and play against it, read below.\
 ```pip install -r path/to/requirements.txt```\
 ```python3 path/to/main.py```

 ## Controls
- W key - move the left paddle up  
- S key - move the left paddle down  

 The right paddle is controlled by the best AI generated (which is stored in the 'best.pickle' file).

 ## Using the AI
 In order to use the AI, you must edit main.py and uncomment line 248. You also need to comment line 251. This will automatically train the model by pitting genomes against one another and playing games of Pong in quick succession. Eventually it will automatically end and output the best AI into the file 'best.pickle' after reaching a fitness level of 100. This number can be tweaked in the config.txt file and a deeper explanation of fitness level can be found [here](https://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf). I will go into deeper explanation on how NEAT works below.

 After training the AI, to use it all you need to do is comment out line 248 and uncomment line 251 (the inverse of what was done at the start).

 # How It Works
 ## Pong Game Overview
 I used pygame to draw my objects, text, and display my window. This was mainly a result of inspiration from the game Drawn Down Abyss from Steam (this game was made through pygame as well). 

I implemented the 'objects' within the Pong game through individual classes to utilize the OOP approach that I learned through AP CSA & CS50P. The classes had attributes that corresponded to the position and size of the objects. The constructor initialized all necessary attributes for each object. Something I realized early into building the game was that I would eventually need to implement a reset position method. To solve the issue for my future self, I ended up utilizing double assignment for the x and y position attributes. This means I stored a temporary value that represented the original position via the constructor. 

Besides the constructor, each class came with a draw, move, and reset method. The draw method utilized the pygame library and the attributes to draw the object on the window using the attributes as a guide. The move method modified the position attributes with the help of input recognition from the pygame library, and the reset method reset the position attributes by referring back to the temporary original position variables I created through the constructor. However, in creating these methods I had to keep the mechanics of the game in mind as well. For instance, the reset method for the ball would not only reset the position of the ball, but also multiply the x component of the velocity by -1 to change the direction of the ball. This would ensure that the opponent that was scored upon would have time to recollect themselves.

Moving on from the classes, there were also a few other methods necessary to the functioning of the game: draw, handle_collision, check_paddle_movement, reset_all, check_win, and handle_score. The check_paddle_movement would check for key presses through pygame and run the object method move for the corresponding object. Reset_all called all of the reset methods for each object in order to reset the entire game (this was necessary after each point/after a player won). Most of these functions are self explanatory. For the most part they utilized simple math and modified the position attributes as needed. For instance, if the ball moved past the right bound of the window, the left player score would be incremented.

**Collision**\
In hindsite, I assumed this project would be a quick and easy job due to the simplicity of the game mechanics and game overall. However, I found myself taking more time than I expected working on the collision for this game. This gives me a new respect for indie game developers who are creating complex games by themselves. Although this game was a simple arcade game it still required a decent amount of math to handle the collision of balls on the paddle. It worked similarly to other methods and used the position of the objects as well as the size of the window to determine whether a collision occurs. Afterwards, the attributes were modified as needed. In theory this sounds simple, but because the different objects were in constant movement, the formulas required to handle said collisions needed to be handled in the abstract which greatly enhanced the difficulty of the project.

## AI Overview
The NEAT algorithm is a type of artificial intelligence (AI) algorithm that is used to train neural networks to solve complex problems. In the context of this code, the NEAT algorithm is being used to train a neural network to play a game of Pong.

The algorithm works by starting with a population of randomly generated neural networks (called "genomes") and evaluating their fitness based on how well they perform in the game. The genomes with the highest fitness scores are then used to create new genomes for the next generation, and the process is repeated. Over time, the genomes evolve to become better and better at playing the game.

In particular, this code calculates fitness in the calculate_fitness() method of the PongGame class. The fitness of the two genomes is calculated based on the results of the game and the duration of the game. The fitness is calculated as the sum of the number of hits made by each paddle and the duration of the game. Specifically, for genome1, the fitness is calculated as game_info.left_hits + duration, and for genome2, the fitness is calculated as game_info.right_hits + duration. The idea is to encourage the paddles to keep the ball in play for as long as possible, while also trying to score points. By using both of these measures, the algorithm can learn to balance the trade-off between scoring points and keeping the ball in play for as long as possible.

Moving on, the NEAT algorithm uses several techniques to ensure that the neural networks continue to evolve and improve over time. One of these techniques is called "speciation," which involves grouping genomes into different "species" based on their similarity. This helps to prevent the algorithm from getting stuck in a local optimum and encourages it to explore a wider range of solutions.

In this code, the NEAT algorithm is being implemented using the neat-python library. The algorithm is being run until a genome reachess a fitness level of 100 according to the config file, and the best genome from each generation is being saved to a file. After the algorithm has finished running, the best genome is loaded from the file and used to create a neural network, which is then tested in a game of Pong. The neural network is able to make decisions about how to move the paddle based on the current state of the game, and over time it evolves to become better and better at playing the game.

# Post-project reflection
When I started working on the project, I had little experience with game development and machine learning. I had some programming experience from previous endeavors, but I knew that creating a Pong AI using NEAT would be a significant undertaking.

As I began working on the project, I quickly realized that there were many aspects to consider, such as designing the game mechanics, implementing the collision detection, and training the AI using the NEAT algorithm. Each of these areas required a different skillset, but I found that my previous programming experience was a great foundation for learning these new concepts.

I used Pygame to draw the game objects and display the window, and I utilized object-oriented programming (OOP) to create classes for the game objects. This allowed me to organize the code in a logical way and made it easier to make changes and additions as needed.

One of the most challenging aspects of the project was implementing the collision detection for the game. It required a lot of math and abstract thinking to handle the collision of the ball on the paddle. However, I persisted and eventually came up with a solution that worked well.

Another significant aspect of the project was training the AI using the NEAT algorithm. I used the neat-python library to implement the algorithm, which involved starting with a population of randomly generated neural networks and evaluating their fitness based on how well they performed in the game. Over time, the genomes evolved to become better at playing the game.

Overall, I found the project to be both challenging and rewarding. It required a lot of time and effort, but I learned a lot about game development and machine learning in the process. I also gained a deeper appreciation for the complexity of indie game development and the amount of work that goes into creating a fun and engaging game.

In the future, I hope to continue exploring the intersection of game development and machine learning and work on more projects that combine these two areas. I am excited to see where this newfound knowledge will take me.




