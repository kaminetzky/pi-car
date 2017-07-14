import RPi.GPIO as GPIO


class Movement:
    def __init__(self):
        self.sensor_pins = {'trig': 11, 'echo': 13}

        GPIO.setmode(GPIO.board)
        GPIO.setwarnings(False)

        GPIO.setup([self.sensor_pins['trig'], GPIO.OUT])
        GPIO.setup([self.sensor_pins['echo'], GPIO.IN])
