import numpy as np
import cv2
from lanes import draw
from PIL import ImageGrab


def draw_lines(image, lines):
    try:
        for i in lines:
            coords = i[0]
            cv2.line(image, (coords[0], coords[1]), (coords[2], coords[3]), [255, 0, 0], 3)
    except:
        pass


def grab():
    return np.array(ImageGrab.grab(bbox=None, all_screens=False))


def process_image(original):
    processed = cv2.Canny(cv2.cvtColor(original, cv2.COLOR_BGR2GRAY), threshold1=300, threshold2=300)
    processed = cv2.GaussianBlur(processed, (5, 5), 0)
    vertices = np.array([[400, 450], [300, 700], [1500, 700], [1400, 450]], np.int32)
    processed = roi(processed, [vertices])
    lines = cv2.HoughLinesP(processed, 1, np.pi / 180, 180, np.array([]), 80, 1)
    m1 = 0
    m2 = 0
    try:
        l1, l2, m1, m2 = draw(original, lines)
        cv2.line(original, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
        cv2.line(original, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        print(str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed, (coords[0], coords[1]), (coords[2], coords[3]), [255, 0, 0], 3)


            except Exception as e:
                print(str(e))
    except Exception as e:
        pass

    return processed, original, m1, m2


def roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked
