import RPi.GPIO as GPIO


class Movement:
    def __init__(self):
        self.sensor_pins = {'trig': 17, 'echo': 27}

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup([self.sensor_pins['trig'], GPIO.OUT])
        GPIO.setup([self.sensor_pins['echo'], GPIO.IN])
