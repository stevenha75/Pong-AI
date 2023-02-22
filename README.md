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
 **Pong Game Overview**\
 I used pygame to draw my objects, text, and display my window. This was mainly a result of inspiration from the game Drawn Down Abyss from Steam (this game was made through pygame as well). 

I implemented the 'objects' within the Pong game through individual classes to utilize the OOP approach that I learned through AP CSA & CS50P. The classes had attributes that corresponded to the position and size of the object. Besides the constructor, each class came with a draw, move, and reset method. The draw method utilized the pygame library and the attributes to draw the object on the window. The move method modified the position attributes, and the reset method reset those position attributes.

**Collision & Movement**

