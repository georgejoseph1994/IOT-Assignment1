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
        B = [0,0,128]
        Y = [255,255,0]
        self.sense.low_light = True

        smiling_face_1 = [W, W, W, W, W, W, W, W,
                          W, W, W, W, W, W, W, W,
                          W, W, R, W, W, R, W, W,
                          W, W, W, W, W, W, W, W,
                          W, W, W, W, W, W, W, W,
                          W, R, W, W, W, W, R, W,
                          W, R, R, R, R, R, R, W,
                          W, W, W, W, W, W, W, W
                          ]

        smiling_face_2 = [Y, Y, Y, Y, Y, Y, Y, Y,
                          Y, Y, R, Y, Y, R, Y, Y,
                          Y, Y, R, Y, Y, R, Y, Y,
                          Y, Y, Y, Y, Y, Y, Y, Y,
                          Y, B, Y, Y, Y, Y, B, Y,
                          Y, B, Y, Y, Y, Y, B, Y,
                          Y, Y, B, B, B, B, Y, Y,
                          Y, Y, Y, Y, Y, Y, Y, Y
                          ]

        smiling_face_3 = [B, B, B, B, B, B, B, B,
                          B, G, G, B, B, G, G, B,
                          B, G, G, B, B, G, G, B,
                          B, B, B, B, B, B, B, B,
                          B, B, R, R, R, R, B, B,
                          B, R, B, B, B, B, R, B,
                          B, R, B, B, B, B, R, B,
                          B, B, B, B, B, B, B, B
                          ]
        try:                  
            while(True):
                self.sense.set_pixels(smiling_face_1)
                time.sleep(3)
                self.sense.clear()
                self.sense.set_pixels(smiling_face_2)
                time.sleep(3)
                self.sense.clear()
                self.sense.set_pixels(smiling_face_3)
                time.sleep(3)
                self.sense.clear()
        finally:
            self.sense.clear()


# Invoking the AnimatedEmoji class method Display
animatedEmoji = AnimatedEmoji()
animatedEmoji.display()
