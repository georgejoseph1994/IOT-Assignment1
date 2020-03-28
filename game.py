from sense_hat import SenseHat
from electronicDie import ElectronicDie

class Game:
    def __init__(self):
        self.electronicDie = ElectronicDie()
        self.sense = SenseHat()
        self.player1Score = 0
        self.player2Score = 0
    
    def startGame(self):
