from sense_hat import SenseHat
from electronicDie import ElectronicDie
from time import sleep
import csv
from datetime import datetime

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
class Game:
    def __init__(self):
        self.electronicDie = ElectronicDie()
        self.sense = SenseHat()
        self.player1 = Player('P1')
        self.player2 = Player('P2')
    
    def performPlayerTurn(self, player):
        player.score+= self.electronicDie.checkForShake(player.name + "'s turn")

    
    def startGame(self):
        self.sense.show_message("Electronic Die Game", scroll_speed=0.08, text_colour=[0, 0, 255])
        sleep(1)
        self.sense.show_message("This is a two player game", scroll_speed=0.06, text_colour=[0, 0, 255])
        sleep(1)
        self.sense.show_message("Each player takes turns to roll the die", scroll_speed=0.06, text_colour=[0, 0, 255])
        sleep(1)
        self.sense.show_message("First player to score above 30 wins", scroll_speed=0.06, text_colour=[0, 0, 255])
        sleep(1)
        self.sense.show_message("Get ready to play...", scroll_speed=0.06, text_colour=[0, 0, 255])
        currentPlayer = self.player1
        while(self.player1.score<=30 and self.player2.score<=30):
            self.performPlayerTurn(currentPlayer)
            currentPlayer = self.player2 if currentPlayer==self.player1 else self.player1
            if currentPlayer==self.player1:
                self.sense.show_message("Score", scroll_speed=0.06, text_colour=[155, 155, 0])
                self.sense.show_message(self.player1.name + ":" + str(self.player1.score), scroll_speed=0.06, text_colour=[155, 155, 0])
                sleep(1)
                self.sense.show_message(self.player2.name + ":" + str(self.player2.score), scroll_speed=0.06, text_colour=[155, 155, 0])
                print(self.player1.name + ":" + str(self.player1.score))
                print(self.player2.name + ":" + str(self.player2.score))
        winner = self.player1 if self.player1.score>30 else self.player2
        self.sense.show_message("Winner is " + winner.name + " with " + str(winner.score) + " points", scroll_speed=0.06, text_colour=[0, 255, 0])
        print("Winner is " + winner.name + " with " + str(winner.score))
        f = open('winner.csv', 'a')
        with f:
            writer = csv.writer(f)
            writer.writerow([winner.name, str(winner.score), datetime.now()])

def main():
    game = Game()
    game.startGame()


if __name__ == "__main__":
    main()