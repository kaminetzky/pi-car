import pygame
import time
from motors import Motors

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
Motors()

while True:
    pygame.event.get()
    left = joystick.get_axis(1)
    right = joystick.get_axis(3)

    if left > 0:
        Motors.left_forward()
    elif left < 0:
        Motors.left_backwards()
    else:
        Motors.left_stop()
    if right > 0:
        Motors.right_forward()
    elif right < 0:
        Motors.right_backwards()
    else:
        Motors.right_stop()

    time.sleep(0.02)
