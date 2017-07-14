import RPi.GPIO as GPIO

from server.motors import Motors

if __name__ == '__main__':
    Motors()
    dict_methods = {'w': Motors.forward_time,
                    'a': Motors.left_time,
                    's': Motors.backwards_time,
                    'd': Motors.right_time}
    while True:
        command = input('Ingrese un comando: ')
        if command == 'exit':
            break
        letter = command[0]
        secs = float(command[1:])
        dict_methods[letter](secs)

    GPIO.cleanup()