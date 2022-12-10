# Project mos jul the runner

# About this project

in this game , you are the character name mos that stuck in somewhere,
and you have to escape by using you parkour ability to dodge obstacles
if you not make it game over .
after pass all the stage (now only have 2 stage)the game will show
scoreboard update into 'User_data.json' file

## Project overview and features

* User can control player character by using W,A,S,D key and Q to quit the game
* Score is count by current stage and time user play by second
* user can use wall jump by heading to the wall and using W key
* Player can't be afk for 5 second if you try you will fall
* Scoreboard will show all player name, stage,and time play

## Requirement libraries and tools

### python version

* Python 3.10 or better

### module

* 'Turtle'
* 'time'
* 'json'

## Program design

There are 5 classes

* `Screen_display`: This class for creating Screen and
  combine all functions to run entire game.
* `Timer`: This class use to collect time use.
* `Player`: This class for create and control player movement.
* `Score`: this class for write and read a score in 'user_data.json' file.
* `Map`: This class for create item and check that player collect item or not.

## Code structure

This project has 5 main file which are "main.py", "score.py", "content.py",
"screen_content.py", "user_data.json"

### 1. "main.py"

This module implements main program menu and collecting username

### 2. "score.py"

This module contains the `Score` class.

### 3. "content.py"

This module contains the `Map`, `player`, `timer` class.

### 4. "screen_content.py"

This module contains the `Screen_display` class.

### 5. "user_data.json"

json file for collecting player stage and time from "score.py"

## attention

I develop this program in mac, so I'm not sure what will happen in window.