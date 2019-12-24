import numpy as np
import cv2
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
    processed = cv2.Canny(cv2.cvtColor(original, cv2.COLOR_BGR2GRAY), threshold1=200, threshold2=250)
    processed = cv2.GaussianBlur(original, (5, 5), 0)
    vertices = np.array([[400, 450], [300, 700], [1500, 700], [1400, 450]])
    processed = roi(processed, [vertices])
    lines = cv2.HoughLinesP(processed, 1, np.pi / 180, 180, np.array([]), 5, 5)
    draw_lines(processed, lines)
    return processed


def roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked
