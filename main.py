import time
import cv2
import input
from image_processing import grab, process_image
from sendkeys import ReleaseKey, PressKey, UP, DOWN, LEFT, RIGHT
import atexit


def on_exit():
    ReleaseKey(UP)
    ReleaseKey(DOWN)
    ReleaseKey(LEFT)
    ReleaseKey(RIGHT)


def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()
    cv2.namedWindow("window2", cv2.WINDOW_NORMAL)
    while True:
        screen = grab()
        new_screen, original, m1, m2 = process_image(screen)
        cv2.imshow('window2', new_screen)
        # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGRA2RGB))
        print("Frame took {} seconds".format(time.time() - last_time))
        last_time = time.time()

        if m1 < 0 and m2 < 0:
            input.right()
        elif m1 > 0 and m2 > 0:
            input.left()
        else:
            input.straight()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()
atexit.register(on_exit)
