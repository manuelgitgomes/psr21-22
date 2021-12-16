#!/usr/bin/python3
import copy
from functools import partial
import numpy as np
import cv2


def main():
    # Creating image
    img = cv2.imread('/Part05/imgs/atlascar.png')

    # Window name definition
    window_name = 'window - Ex1c'

    # Creating window
    cv2.namedWindow(window_name)

    # Image shape
    h, w, _ = img.shape

    # Drawing a circle and placing test
    cv2.circle(img, (int(w/2), int(h/2)), 200, (255, 0, 0), 5)
    cv2.putText(img, 'PSR', (int(w/2), int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    # Show image
    cv2.imshow(window_name, img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()