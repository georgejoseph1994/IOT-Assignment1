# [Task a]
# (5 marks)
# Create a python file called animatedEmoji.py Which Will display 3 Emoji faces in the LED matrix on Sense HAT.
# You need to create your oWn Emoji With at least 3 colours for each. You also need to display them one by one With 3 seconds interval.

from sense_hat import SenseHat
import time


class AnimatedEmoji:
    sense = None

    def __init__(self):
        self.sense = SenseHat()

    def display(self):
        R = [255, 0, 0]  # Red
        W = [255, 255, 255]  # White
        G = [0, 128, 0]  # Green

        self.sense.low_light = True

        smiling_face = [W, W, W, W, W, W, W, W,
                        W, W, W, W, W, W, W, W,
                        W, W, R, W, W, R, W, W,
                        W, W, W, W, W, W, W, W,
                        W, W, W, W, W, W, W, W,
                        W, R, W, W, W, W, R, W,
                        W, R, R, R, R, R, R, W,
                        W, W, W, W, W, W, W, W
                        ]
        self.sense.set_pixels(smiling_face)
        time.sleep(5)
        self.sense.clear()

# Invoking the AnimatedEmoji class method Display
animatedEmoji = AnimatedEmoji()
animatedEmoji.display()
