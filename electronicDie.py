from sense_hat import SenseHat
from random import choice
from time import sleep

class ElectronicDie:

    def __init__(self):
        self.value = None
        X = [0, 255, 0]  
        O = [0, 0, 0] 
        self.values = self.updateValues(X, O) 
        self.sense = SenseHat()

    def checkForShake(self, message):
        flag = False
        self.sense.show_message(message, scroll_speed=0.06)
        while flag==False:
            x, y, z = self.sense.get_accelerometer_raw().values()
            if abs(x) > 2 or abs(y) > 2 or abs(z) > 2:
                self.animateShaking()
                self.value=choice(self.values)
                self.sense.set_pixels(self.value['pixels'])
                flag=True
                sleep(2)
                return self.value['number']
    
    def animateShaking(self):
        X = [155, 155, 0]  
        O = [0, 0, 0]
        self.values = self.updateValues(X, O) 
        i=0
        while i<4:
            for item in self.values: 
                self.sense.set_pixels(item['pixels'])
                sleep(0.1)
            i+=1
        X = [0, 255, 0]  
        O = [0, 0, 0] 
        self.values = self.updateValues(X, O) 

    def updateValues(self, X, O):
        return [
            {   'number': '1',
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
            {   'number': '2',
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
            {   'number': '3',
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
            {   'number': '4',
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
            {   'number': '5',
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
            {   'number': '6',
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

                
                

die =  ElectronicDie()
value = die.checkForShake('Shake now!')
sense = SenseHat()
sense.show_letter(value, [0, 255, 0])
sleep(2)
sense.clear()