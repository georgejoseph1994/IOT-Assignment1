from sense_hat import SenseHat
from random import choice
from time import sleep

class ElectronicDie:

    def __init__(self):
        self.value = None
        self.values = ['1', '2', '3', '4', '5', '6']
        self.sense = SenseHat()

    def checkForShake(self, message):
        flag = False
        self.sense.show_message(message, scroll_speed=0.06)
        while flag==False:
            x, y, z = self.sense.get_accelerometer_raw().values()
            if abs(x) > 2 or abs(y) > 2 or abs(z) > 2:
                self.sense.show_letter(choice(self.values), [0, 255, 0])
                flag=True
                sleep(5)
                self.sense.clear();
                

die =  ElectronicDie();
die.checkForShake('Shake now!');


