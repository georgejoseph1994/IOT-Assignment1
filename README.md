# IOT-Assignment1

## Animated Emoji
This program displays 3 emoji faces in Sense HAT LED matrix in 3 second interval.

`python3 animatedEmoji.py`

## Temperature Monitoring and display
This program displays temperature in the sense HAT display. Temperature ranges are stored in config.json.
* If the level of temperature is cold, display temperature with blue colour.
* If the level of temperature is comfortable, display temperature with green colour.
* If the level of temperature is hot, display temperature with red colour.


`python3 monitorAndDisplay.py`

## The electronic die program
This program displays a message and awaits the user to shake the raspberrypi with the sensehat. Upon shaking, the sensehat displays a random number (0 to 6) just like an ordinary die. To run the electronic die program, execute 
the following command

`python3 electronicDie.py`

## The electronic die game
This program simulates the two player game.
Each player takes turns rolling the die.
The first player to score above 30 wins.
The winner of the game (P1 or P2) will be written into a file called winner.csv with the score and the timestamp.
To run the game program, execute the following command

`python3 game.py`

