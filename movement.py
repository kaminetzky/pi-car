import RPi.GPIO as GPIO


class Movement:
    def __init__(self):
        self.motor_pins = [5, 6, 13, 19]

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup([self.motor_pins], GPIO.OUT)
