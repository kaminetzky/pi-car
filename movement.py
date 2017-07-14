import RPi.GPIO as GPIO
import time


class Movement:
    def __init__(self):
        self.pins = {'a_1': 5, 'a_2': 6, 'b_2': 13, 'b_1': 19}

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(list(self.pins.values()), GPIO.OUT)

    def forward(self):
        self.stop()
        GPIO.output([self.pins['a_1'], self.pins['b_1']], True)

    def backwards(self):
        self.stop()
        GPIO.output([self.pins['a_2'], self.pins['b_2']], True)

    def left(self):
        self.stop()
        GPIO.output([self.pins['a_1'], self.pins['b_2']], True)

    def right(self):
        self.stop()
        GPIO.output([self.pins['a_2'], self.pins['b_1']], True)

    def stop(self):
        GPIO.output(list(self.pins.values()), False)


if __name__ == '__main__':
    movement = Movement()
    movement.forward()
    time.sleep(1)
    movement.backwards()
    time.sleep(1)
    movement.left()
    time.sleep(1)
    movement.right()
    time.sleep(1)
    movement.stop()
    
    GPIO.cleanup()
