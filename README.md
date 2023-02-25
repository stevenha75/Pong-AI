# Pong AI - CS50P Final Project
 Recreation of Pong that utilizes ____, a machine learning algorithm. This is currently in development and a task list can be found below.

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
- [Post-project reflection](https://github.com/stevenha75/Pong-AI#ai-overview)

## Task List
 - [x] Implement Pong itself
 - [x] Write Simple Unit Tests
 - [x] Create a demo video following the guidelines provided by Harvard
 - [ ] Submit Final Project
 - [ ] Implement AI for the game
 - [ ] Create a main menu screen
 - [ ] Finish the README.md

 ## Video Demo
<iframe width="560" height="315" src="https://www.youtube.com/embed/TM2VOzjg8Xg" frameborder="0" allowfullscreen></iframe>

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

I implemented the 'objects' within the Pong game through individual classes to utilize the OOP approach that I learned through AP CSA & CS50P. The classes had attributes that corresponded to the position and size of the objects. The constructor initialized all necessary attributes for each object. Something I realized early into building the game was that I would eventually need to implement a reset position method. To solve the issue for my future self, I ended up utilizing double assignment for the x and y position attributes. This means I stored a temporary value that represented the original position via the constructor. 

Besides the constructor, each class came with a draw, move, and reset method. The draw method utilized the pygame library and the attributes to draw the object on the window using the attributes as a guide. The move method modified the position attributes with the help of input recognition from the pygame library, and the reset method reset the position attributes by referring back to the temporary original position variables I created through the constructor. However, in creating these methods I had to keep the mechanics of the game in mind as well. For instance, the reset method for the ball would not only reset the position of the ball, but also multiply the x component of the velocity by -1 to change the direction of the ball. This would ensure that the opponent that was scored upon would have time to recollect themselves.

Moving on from the classes, there were also a few other methods necessary to the functioning of the game: draw, handle_collision, check_paddle_movement, reset_all, check_win, and handle_score. The check_paddle_movement would check for key presses through pygame and run the object method move for the corresponding object. Reset_all called all of the reset methods for each object in order to reset the entire game (this was necessary after each point/after a player won). Most of these functions are self explanatory. For the most part they utilized simple math and modified the position attributes as needed. For instance, if the ball moved past the right bound of the window, the left player score would be incremented.

**Collision**\
In hindsite, I assumed this project would be a quick and easy job due to the simplicity of the game mechanics and game overall. However, I found myself taking more time than I expected working on the collision for this game. This gives me a new respect for indie game developers who are creating complex games by themselves. Although this game was a simple arcade game it still required a decent amount of math to handle the collision of balls on the paddle. It worked similarly to other methods and used the position of the objects as well as the size of the window to determine whether a collision occurs. Afterwards, the attributes were modified as needed. In theory this sounds simple, but because the different objects were in constant movement, the formulas required to handle said collisions needed to be handled in the abstract which greatly enhanced the difficulty of the project.

## AI Overview
