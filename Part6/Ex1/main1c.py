#!/usr/bin/python3
import copy
from functools import partial
import numpy as np
import cv2


def onMouse(curr, posx, posy, last, a, image, colour):
    global pressed

    if colour == 'r':
        ccode = (0, 0, 255)
    elif colour == 'g':
        ccode = (0, 255, 0)
    elif colour == 'b':
        ccode = (255, 0, 0)
    else:
        ccode = (255, 0, 0)

    if curr == cv2.EVENT_LBUTTONUP:
        pressed = False
    elif curr == cv2.EVENT_LBUTTONDOWN:
        pressed = True
    if pressed:
        print(ccode)
        cv2.circle(image, (posx, posy), 3, ccode, -1)


def main():
    global pressed

    # Creating image
    img_r = np.zeros([400, 600, 1], dtype=np.uint8)
    img_r.fill(255)
    img_g = copy.deepcopy(img_r)
    img_b = copy.deepcopy(img_r)
    img = cv2.merge([img_b, img_g, img_r])

    # Window name definition
    window_name = 'window - Ex1c'

    # Show white image
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, img)

    # Default colour and key
    colour = 'r'
    key = -1
    pressed = False

    # Using partial
    onMouseLite = partial(onMouse, image=img)

    while True:
        if key == ord('r'):
            colour = 'r'
        elif key == ord('g'):
            colour = 'g'
        elif key == ord('b'):
            colour = 'b'

        onMouseFull = partial(onMouseLite, colour=colour)

        cv2.setMouseCallback(window_name, onMouseFull)
        cv2.imshow(window_name, img)
        key = cv2.waitKey(1)

if __name__ == '__main__':
    main()