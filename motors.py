import RPi.GPIO as GPIO
import time


class Movement:
    def __init__(self):
        self.pins = {'a_1': 5, 'a_2': 6, 'b_2': 13, 'b_1': 19}

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(list(self.pins.values()), GPIO.OUT)

    def stop(self):
        GPIO.output(list(self.pins.values()), False)

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

    def forward_time(self, seconds):
        self.forward()
        time.sleep(seconds)
        self.stop()

    def backwards_time(self, seconds):
        self.backwards()
        time.sleep(seconds)
        self.stop()

    def left_time(self, seconds):
        self.left()
        time.sleep(seconds)
        self.stop()

    def right_time(self, seconds):
        self.right()
        time.sleep(seconds)
        self.stop()


if __name__ == '__main__':
    movement = Movement()
    dict_methods = {'w': movement.forward_time,
                    'a': movement.left_time,
                    's': movement.backwards_time,
                    'd': movement.right_time}
    while True:
        command = input('Ingrese un comando: ')
        if command == 'exit':
            break
        letter = command[0]
        secs = float(command[1:])
        dict_methods[letter](secs)

    GPIO.cleanup()
