import RPi.GPIO as GPIO
import time

class Movement:
    def __init__(self):
        self.motor_pins = [5, 6, 13, 19]

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.motor_pins, GPIO.OUT)

    def forward(self):
        GPIO.output([self.motor_pins[0], self.motor_pins[2]], True)

    def stop(self):
        GPIO.output(self.motor_pins, False)


if __name__ == '__main__':
    movement = Movement()
    movement.forward()
    time.sleep(2)
    movement.stop()
    GPIO.cleanup()
