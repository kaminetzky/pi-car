import RPi.GPIO as GPIO


class Movement:
    def __init__(self):
        self.motor_pins = [29, 31, 33, 35]

        GPIO.setmode(GPIO.board)
        GPIO.setwarnings(False)

        GPIO.setup([self.motor_pins], GPIO.OUT)