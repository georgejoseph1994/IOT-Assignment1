from sense_hat import SenseHat
from electronicDie import ElectronicDie
from time import sleep
import csv
from datetime import datetime

# Player class is used to store the details of a player
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
# Game class is used form a game instance
class Game:
    def __init__(self):
        self.electronicDie = ElectronicDie()
        self.sense = SenseHat()
        self.player1 = Player('P1')
        self.player2 = Player('P2')
    
    # This method implements the requesting and waiting for player to interact with the die
    def performPlayerTurn(self, player):
        player.score+= self.electronicDie.checkForShake(player.name + "'s turn")

    # This method displays the instructions
    def showInstructions(self):
        self.sense.show_message("Electronic Die Game", scroll_speed=0.08, 
                                text_colour=[0, 0, 255])
        sleep(1)
        self.sense.show_message("This is a two player game", scroll_speed=0.06, 
                                text_colour=[0, 0, 255])
        sleep(1)
        self.sense.show_message("Each player takes turns to roll the die", 
                                scroll_speed=0.06, 
                                text_colour=[0, 0, 255])
        sleep(1)
        self.sense.show_message("First player to score above 30 wins", 
                                scroll_speed=0.06, 
                                text_colour=[0, 0, 255])
        sleep(1)
        self.sense.show_message("Get ready to play...", scroll_speed=0.06, 
                                text_colour=[0, 0, 255])

    # This method starts the game    
    def startGame(self):
        self.showInstructions()
        currentPlayer = self.player1

        while(self.player1.score<=30 and self.player2.score<=30):
            self.performPlayerTurn(currentPlayer)

            #Switch player
            if currentPlayer==self.player1:
                currentPlayer = self.player2 
            else:
                currentPlayer = self.player1

            if currentPlayer==self.player1:
                self.displayScore()

        winner = self.player1 if self.player1.score>30 else self.player2
        self.sense.show_message("Winner is " + winner.name + " with " + 
                                str(winner.score) + " points", 
                                scroll_speed=0.06, 
                                text_colour=[0, 255, 0])
        print("Winner is " + winner.name + " with " + str(winner.score))
        
        # Write the winner to csv file
        f = open('winner.csv', 'a')
        with f:
            writer = csv.writer(f)
            writer.writerow([winner.name, str(winner.score), datetime.now()])

    # This method displays the score
    def displayScore(self):     
        self.sense.show_message("Score", scroll_speed=0.06, 
                                        text_colour=[155, 155, 0])
        self.sense.show_message(self.player1.name + ":" + str(self.player1.score), 
                                scroll_speed=0.06, text_colour=[155, 155, 0])
        sleep(1)
        self.sense.show_message(self.player2.name + ":" + str(self.player2.score), 
                                scroll_speed=0.06, text_colour=[155, 155, 0])
        print(self.player1.name + ":" + str(self.player1.score))
        print(self.player2.name + ":" + str(self.player2.score)) 


def main():
    game = Game()
    game.startGame()


if __name__ == "__main__":
    main()