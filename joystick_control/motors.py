import RPi.GPIO as GPIO
import time


class Motors:
    pins = {'a_en': 10, 'b_en': 9, 'a_1': 5, 'a_2': 6, 'b_2': 13, 'b_1': 19}
    a_en = None
    b_en = None
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(list(Motors.pins.values()), GPIO.OUT)

        Motors.a_en = GPIO.PWM(Motors.pins['a_en'], 100)
        Motors.b_en = GPIO.PWM(Motors.pins['b_en'], 100)
        Motors.a_en.start(100)
        Motors.b_en.start(100)

    @staticmethod
    def stop():
        GPIO.output([Motors.pins['a_1'], Motors.pins['a_2'],
                     Motors.pins['b_1'], Motors.pins['b_2']], False)

    @staticmethod
    def forward():
        Motors.stop()
        GPIO.output([Motors.pins['a_1'], Motors.pins['b_1']], True)

    @staticmethod
    def backwards():
        Motors.stop()
        GPIO.output([Motors.pins['a_2'], Motors.pins['b_2']], True)

    @staticmethod
    def left():
        Motors.stop()
        GPIO.output([Motors.pins['a_2'], Motors.pins['b_1']], True)

    @staticmethod
    def right():
        Motors.stop()
        GPIO.output([Motors.pins['a_1'], Motors.pins['b_2']], True)

    @staticmethod
    def forward_time(seconds):
        Motors.forward()
        time.sleep(seconds)
        Motors.stop()

    @staticmethod
    def backwards_time(seconds):
        Motors.backwards()
        time.sleep(seconds)
        Motors.stop()

    @staticmethod
    def left_time(seconds):
        Motors.left()
        time.sleep(seconds)
        Motors.stop()

    @staticmethod
    def right_time(seconds):
        Motors.right()
        time.sleep(seconds)
        Motors.stop()

    @staticmethod
    def left_forward(speed=1):
        Motors.a_en.ChangeDutyCycle(speed * 100)
        GPIO.output(Motors.pins['a_1'], True)
        GPIO.output(Motors.pins['a_2'], False)

    @staticmethod
    def left_backwards(speed=1):
        Motors.a_en.ChangeDutyCycle(speed * 100)
        GPIO.output(Motors.pins['a_1'], False)
        GPIO.output(Motors.pins['a_2'], True)

    @staticmethod
    def left_stop():
        GPIO.output(Motors.pins['a_1'], False)
        GPIO.output(Motors.pins['a_2'], False)

    @staticmethod
    def right_forward(speed=1):
        Motors.b_en.ChangeDutyCycle(speed * 100)
        GPIO.output(Motors.pins['b_1'], True)
        GPIO.output(Motors.pins['b_2'], False)

    @staticmethod
    def right_backwards(speed=1):
        Motors.b_en.ChangeDutyCycle(speed * 100)
        GPIO.output(Motors.pins['b_1'], False)
        GPIO.output(Motors.pins['b_2'], True)

    @staticmethod
    def right_stop():
        GPIO.output(Motors.pins['b_1'], False)
        GPIO.output(Motors.pins['b_2'], False)
