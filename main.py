import RPi.GPIO as GPIO
from motors import Motors

if __name__ == '__main__':
    motors = Motors()
    dict_methods = {'w': motors.forward_time,
                    'a': motors.left_time,
                    's': motors.backwards_time,
                    'd': motors.right_time}
    while True:
        command = input('Ingrese un comando: ')
        if command == 'exit':
            break
        letter = command[0]
        secs = float(command[1:])
        dict_methods[letter](secs)

    GPIO.cleanup()