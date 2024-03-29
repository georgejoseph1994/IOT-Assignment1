from sense_hat import SenseHat
from random import choice
from time import sleep

class ElectronicDie:

    def __init__(self):
        self.value = None
        X = [0, 255, 0]  
        O = [0, 0, 0] 
        self.values = self.update_values(X, O) 
        self.sense = SenseHat()

    # This method checks for rolling of the die
    def check_for_shake(self, message):
        flag = False
        self.sense.show_message(message, scroll_speed=0.06, 
                                text_colour=[0, 0, 255])
        i = 0
        while flag==False:
            x, y, z = self.sense.get_accelerometer_raw().values()
            if abs(x) > 2 or abs(y) > 2 or abs(z) > 2:
                self.animate_shaking()
                self.value=choice(self.values)
                self.sense.set_pixels(self.value['pixels'])
                flag=True
                sleep(2)
                return self.value['number']
            i+=1
            if i%200==0:
                self.sense.show_message(message, scroll_speed=0.06, 
                                        text_colour=[0, 0, 255])
    
    # This method displays the animation for a roll taking place
    def animate_shaking(self):
        X = [155, 155, 0]  
        O = [0, 0, 0]
        self.values = self.update_values(X, O) 
        i=0
        while i<4:
            for item in self.values: 
                self.sense.set_pixels(item['pixels'])
                sleep(0.1)
            i+=1
        X = [0, 255, 0]  
        O = [0, 0, 0] 
        self.values = self.update_values(X, O) 

    # This method sets the pixels values for each number of the die
    # The parameters decide the color of the die
    def update_values(self, X, O):
        return [
            {   'number': 1,
                'pixels':[
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O,
                    O, O, O, X, X, O, O, O,
                    O, O, O, X, X, O, O, O,
                    O, O, O, O, O, O, O, O, 
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O
                ]
            },
            {   'number': 2,
                'pixels':[
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, X, X, O,
                    O, O, O, O, O, X, X, O,
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O,
                    O, X, X, O, O, O, O, O,
                    O, X, X, O, O, O, O, O,
                    O, O, O, O, O, O, O, O
                ]
            },
            {   'number': 3,
                'pixels':[
                    O, O, O, O, O, O, X, X,
                    O, O, O, O, O, O, X, X,
                    O, O, O, O, O, O, O, O,
                    O, O, O, X, X, O, O, O,
                    O, O, O, X, X, O, O, O,
                    O, O, O, O, O, O, O, O,
                    X, X, O, O, O, O, O, O,
                    X, X, O, O, O, O, O, O
                ]
            },
            {   'number': 4,
                'pixels':[
                    O, O, O, O, O, O, O, O,
                    O, X, X, O, O, X, X, O,
                    O, X, X, O, O, X, X, O,
                    O, O, O, O, O, O, O, O,
                    O, O, O, O, O, O, O, O,
                    O, X, X, O, O, X, X, O,
                    O, X, X, O, O, X, X, O,
                    O, O, O, O, O, O, O, O
                ]

            },
            {   'number': 5,
                'pixels':[
                    X, X, O, O, O, O, X, X,
                    X, X, O, O, O, O, X, X,
                    O, O, O, O, O, O, O, O,
                    O, O, O, X, X, O, O, O,
                    O, O, O, X, X, O, O, O,
                    O, O, O, O, O, O, O, O,
                    X, X, O, O, O, O, X, X,
                    X, X, O, O, O, O, X, X
                ]
            },
            {   'number': 6,
                'pixels':[
                    O, X, X, O, O, X, X, O,
                    O, X, X, O, O, X, X, O,
                    O, O, O, O, O, O, O, O,
                    O, X, X, O, O, X, X, O,
                    O, X, X, O, O, X, X, O,
                    O, O, O, O, O, O, O, O,
                    O, X, X, O, O, X, X, O,
                    O, X, X, O, O, X, X, O
                ]
            }
        ]

                
                
def main():
    die =  ElectronicDie()
    die.check_for_shake('Shake now!')
    sense = SenseHat()
    sleep(2)
    sense.clear()


if __name__ == "__main__":
    main()
