# Pong AI - CS50P Final Project
 Recreation of Pong that utilizes NEAT (NeuroEvolution of Augmenting Topologies), a machine learning algorithm. This is currently still in development and a task list can be found below.

## Table of Contents
- Task List
- Video Demo
- Installation & Usage
    - Dependencies
    - Installation
    - Controls
    - Using the AI
- How It Works

## Task List
 - [x] Implement Pong itself
 - [x] Comment code 
 - [x] Write Simple Unit Tests
 - [ ] Update README.md w/ detailed explanations
 - [ ] Create an demo video following the guidelines provided by Harvard
 - [ ] Submit Final Project
 - [ ] Implement & comment AI for the game
 - [ ] Write a section to explain the AI

 ## Video Demo


 # Installation & Usage

   ## Dependencies
 - [Pygame](https://www.pygame.org/wiki/GettingStarted)
 - [Python](https://www.python.org/downloads/)

 ## Installation
 1. First clone the repository\
 ```git clone https://github.com/stevenha75/kickproxies/git```
 2. Install dependencies then run main.py\
 ```python3 -m pip install -U pygame --user```\
 ```python3 path/to/main.py```

 ## Controls

 ## Using the AI

 # How It Works
 ## Pong Game Overview
 I used pygame to draw my objects, text, and display my window. This was mainly a result of inspiration from the game Drawn Down Abyss from Steam (this game was made through pygame as well). 

I implemented the 'objects' within the Pong game through individual classes to utilize the OOP approach that I learned through AP CSA & CS50P. The classes had attributes that corresponded to the position and size of the object. The constructor initialized all necessary attributes for each object. Something I realized early into building the game was that I would eventually need to implement a reset position method. To solve the issue for my future self, I ended up utilizing double assignment for the x and y position attributes. This means I stored a temporary value that represented the original position via the constructor for the position attributes. 

Besides the constructor, each class came with a draw, move, and reset method. The draw method utilized the pygame library and the attributes to draw the object on the window using the attributes as a guide. The move method modified the position attributes with the help of input recognition from the pygame library, and the reset method reset the position attributes by referring back to the temporary original position variables I created through the constructor. However, in creating these methods I had to keep the mechanics of the game in mind as well. For instance, the reset method for the ball would not only reset the position of the ball, but also multiply the x component of the velocity by -1 to change the direction of the ball. This would ensure that the opponent that was scored upon would have time to recollect themselves.

Moving on from the classes, there were also a few other methods necessary to the functioning of the game: draw, handle_collision, check_paddle_movement, reset_all, check_win, and hangle_score. The check_paddle_movement would check for key presses through pygame and run the object method move for the corresponding object. Reset_all called all of the reset methods for each object in order to reset the entire game (this was necessary after each point/after a player won). Most of these functions are self explanatory.

**Collision**\
In hindsite, I assumed this project would be a quick and easy job due to the simplicity of the game mechanics and game overall. However, I found myself taking more time than I expected working on the collision for this game. This gives me a new respect for indie game developers who are creating complex games by themselves.

## AI Overview
