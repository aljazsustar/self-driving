from sendkeys import PressKey, ReleaseKey, UP, DOWN, LEFT, RIGHT
from time import sleep


def straight():
    PressKey(UP)
    ReleaseKey(LEFT)
    ReleaseKey(RIGHT)


def right():
    PressKey(RIGHT)
    ReleaseKey(LEFT)
    ReleaseKey(RIGHT)


def left():
    PressKey(LEFT)
    ReleaseKey(RIGHT)
    ReleaseKey(LEFT)
