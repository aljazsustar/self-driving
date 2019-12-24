import time
import cv2
from sendkeys import PressKey, ReleaseKey, UP, DOWN, LEFT, RIGHT

from image_processing import grab, process_image


def main():
    last_time = time.time()
    cv2.namedWindow("window2", cv2.WINDOW_NORMAL)
    while True:
        screen = grab()
        new_screen = process_image(screen)
        cv2.imshow('window2', new_screen)
        # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGRA2RGB))
        print("Frame took {} seconds".format(time.time() - last_time))
        last_time = time.time()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()
